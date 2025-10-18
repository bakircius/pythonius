"""
Python Mikroservis Mimarisi - Comprehensive Guide
Service Discovery, Message Queue, Circuit Breaker, Load Balancing

Bu dosyada mikroservis mimarisi prensipleri, servis keşfi, mesaj kuyruğu,
circuit breaker pattern, load balancing ve containerization konuları incelenecek.
"""

import asyncio
import json
import time
import random
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Callable, Any
from enum import Enum
from dataclasses import dataclass, asdict
import hashlib
from contextlib import asynccontextmanager
import threading
from collections import defaultdict, deque
import heapq

# =============================================================================
# 1. MICROSERVICE FOUNDATIONS
# =============================================================================

print("=== Microservice Foundations ===")

class ServiceStatus(Enum):
    """Service status enumeration"""
    STARTING = "starting"
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    STOPPING = "stopping"
    STOPPED = "stopped"

@dataclass
class ServiceInfo:
    """Service information"""
    name: str
    version: str
    host: str
    port: int
    endpoints: List[str]
    status: ServiceStatus
    metadata: Dict[str, Any]
    registered_at: datetime
    last_heartbeat: datetime
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            **asdict(self),
            "status": self.status.value,
            "registered_at": self.registered_at.isoformat(),
            "last_heartbeat": self.last_heartbeat.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ServiceInfo':
        """Create from dictionary"""
        return cls(
            name=data["name"],
            version=data["version"],
            host=data["host"],
            port=data["port"],
            endpoints=data["endpoints"],
            status=ServiceStatus(data["status"]),
            metadata=data["metadata"],
            registered_at=datetime.fromisoformat(data["registered_at"]),
            last_heartbeat=datetime.fromisoformat(data["last_heartbeat"])
        )

class BaseService:
    """Base microservice class"""
    
    def __init__(self, name: str, version: str, host: str = "localhost", port: int = 8000):
        self.name = name
        self.version = version
        self.host = host
        self.port = port
        self.status = ServiceStatus.STOPPED
        self.endpoints = []
        self.metadata = {}
        self.startup_time = None
        self.shutdown_hooks = []
        self.health_checks = []
        
        print(f"🔧 Service initialized: {name} v{version}")
    
    def add_endpoint(self, path: str, method: str = "GET"):
        """Add service endpoint"""
        endpoint = f"{method} {path}"
        if endpoint not in self.endpoints:
            self.endpoints.append(endpoint)
            print(f"📍 Endpoint added: {endpoint}")
    
    def add_health_check(self, check_func: Callable):
        """Add health check function"""
        self.health_checks.append(check_func)
        print(f"🏥 Health check added: {check_func.__name__}")
    
    def add_shutdown_hook(self, hook_func: Callable):
        """Add shutdown hook"""
        self.shutdown_hooks.append(hook_func)
        print(f"🪝 Shutdown hook added: {hook_func.__name__}")
    
    async def start(self):
        """Start the service"""
        self.status = ServiceStatus.STARTING
        self.startup_time = datetime.utcnow()
        
        try:
            await self._initialize()
            self.status = ServiceStatus.HEALTHY
            print(f"✅ Service started: {self.name} on {self.host}:{self.port}")
        except Exception as e:
            self.status = ServiceStatus.UNHEALTHY
            print(f"❌ Failed to start service {self.name}: {str(e)}")
            raise
    
    async def stop(self):
        """Stop the service"""
        self.status = ServiceStatus.STOPPING
        
        # Execute shutdown hooks
        for hook in self.shutdown_hooks:
            try:
                await hook()
            except Exception as e:
                print(f"⚠️ Shutdown hook error: {str(e)}")
        
        await self._cleanup()
        self.status = ServiceStatus.STOPPED
        print(f"🛑 Service stopped: {self.name}")
    
    async def health_check(self) -> Dict[str, Any]:
        """Perform health check"""
        health_status = {
            "service": self.name,
            "version": self.version,
            "status": self.status.value,
            "uptime": self._get_uptime(),
            "checks": {}
        }
        
        # Run custom health checks
        for i, check in enumerate(self.health_checks):
            try:
                result = await check()
                health_status["checks"][f"check_{i}"] = {
                    "status": "healthy" if result else "unhealthy",
                    "message": "OK" if result else "Check failed"
                }
            except Exception as e:
                health_status["checks"][f"check_{i}"] = {
                    "status": "error",
                    "message": str(e)
                }
        
        # Overall health assessment
        unhealthy_checks = [c for c in health_status["checks"].values() 
                          if c["status"] != "healthy"]
        
        if unhealthy_checks:
            if self.status == ServiceStatus.HEALTHY:
                self.status = ServiceStatus.DEGRADED
        elif self.status == ServiceStatus.DEGRADED:
            self.status = ServiceStatus.HEALTHY
        
        return health_status
    
    def _get_uptime(self) -> Optional[str]:
        """Get service uptime"""
        if not self.startup_time:
            return None
        
        uptime = datetime.utcnow() - self.startup_time
        return str(uptime)
    
    async def _initialize(self):
        """Override in subclasses"""
        pass
    
    async def _cleanup(self):
        """Override in subclasses"""
        pass

# Service implementations
class UserService(BaseService):
    """User management microservice"""
    
    def __init__(self):
        super().__init__("user-service", "1.0.0", port=8001)
        self.users = {}
        
        # Add endpoints
        self.add_endpoint("/users", "GET")
        self.add_endpoint("/users", "POST")
        self.add_endpoint("/users/{id}", "GET")
        self.add_endpoint("/users/{id}", "PUT")
        self.add_endpoint("/users/{id}", "DELETE")
        
        # Add health check
        self.add_health_check(self._check_database_connection)
    
    async def _initialize(self):
        """Initialize service"""
        # Simulate database connection
        await asyncio.sleep(0.1)
        print("📊 User database connected")
    
    async def _check_database_connection(self) -> bool:
        """Check database connection"""
        # Simulate database check
        return random.random() > 0.1  # 90% success rate

class ProductService(BaseService):
    """Product catalog microservice"""
    
    def __init__(self):
        super().__init__("product-service", "1.0.0", port=8002)
        self.products = {}
        
        # Add endpoints
        self.add_endpoint("/products", "GET")
        self.add_endpoint("/products", "POST")
        self.add_endpoint("/products/{id}", "GET")
        self.add_endpoint("/products/search", "GET")
        
        # Add health checks
        self.add_health_check(self._check_inventory_system)
    
    async def _initialize(self):
        """Initialize service"""
        # Simulate inventory system connection
        await asyncio.sleep(0.1)
        print("📦 Inventory system connected")
    
    async def _check_inventory_system(self) -> bool:
        """Check inventory system"""
        return random.random() > 0.05  # 95% success rate

class OrderService(BaseService):
    """Order processing microservice"""
    
    def __init__(self):
        super().__init__("order-service", "1.0.0", port=8003)
        self.orders = {}
        
        # Add endpoints
        self.add_endpoint("/orders", "GET")
        self.add_endpoint("/orders", "POST")
        self.add_endpoint("/orders/{id}", "GET")
        self.add_endpoint("/orders/{id}/status", "PUT")
        
        # Add health checks
        self.add_health_check(self._check_payment_gateway)
    
    async def _initialize(self):
        """Initialize service"""
        # Simulate payment gateway connection
        await asyncio.sleep(0.1)
        print("💳 Payment gateway connected")
    
    async def _check_payment_gateway(self) -> bool:
        """Check payment gateway"""
        return random.random() > 0.02  # 98% success rate

# Service foundation demonstration
print("Microservice foundations örnekleri:")

async def service_foundation_demo():
    # Create services
    user_service = UserService()
    product_service = ProductService()
    order_service = OrderService()
    
    services = [user_service, product_service, order_service]
    
    # Start services
    for service in services:
        await service.start()
    
    # Perform health checks
    print("\n--- Health Checks ---")
    for service in services:
        health = await service.health_check()
        print(f"{service.name}: {health['status']} (uptime: {health['uptime']})")
    
    # Stop services
    for service in services:
        await service.stop()

# Run foundation demo
asyncio.run(service_foundation_demo())

# =============================================================================
# 2. SERVICE DISCOVERY
# =============================================================================

print("\n=== Service Discovery ===")

class ServiceRegistry:
    """Service registry for service discovery"""
    
    def __init__(self):
        self.services: Dict[str, ServiceInfo] = {}
        self.service_instances: Dict[str, List[ServiceInfo]] = defaultdict(list)
        self.heartbeat_timeout = timedelta(seconds=30)
        self._running = False
        self._cleanup_task = None
    
    async def start(self):
        """Start service registry"""
        self._running = True
        self._cleanup_task = asyncio.create_task(self._cleanup_expired_services())
        print("🔍 Service registry started")
    
    async def stop(self):
        """Stop service registry"""
        self._running = False
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
        print("🔍 Service registry stopped")
    
    async def register_service(self, service: BaseService) -> str:
        """Register a service"""
        service_id = f"{service.name}-{uuid.uuid4().hex[:8]}"
        
        service_info = ServiceInfo(
            name=service.name,
            version=service.version,
            host=service.host,
            port=service.port,
            endpoints=service.endpoints.copy(),
            status=service.status,
            metadata=service.metadata.copy(),
            registered_at=datetime.utcnow(),
            last_heartbeat=datetime.utcnow()
        )
        
        self.services[service_id] = service_info
        self.service_instances[service.name].append(service_info)
        
        print(f"📝 Service registered: {service.name} ({service_id})")
        return service_id
    
    async def deregister_service(self, service_id: str):
        """Deregister a service"""
        if service_id in self.services:
            service_info = self.services[service_id]
            
            # Remove from instances list
            if service_info.name in self.service_instances:
                self.service_instances[service_info.name] = [
                    s for s in self.service_instances[service_info.name]
                    if s != service_info
                ]
            
            del self.services[service_id]
            print(f"🗑️ Service deregistered: {service_info.name} ({service_id})")
    
    async def heartbeat(self, service_id: str, status: ServiceStatus = None):
        """Update service heartbeat"""
        if service_id in self.services:
            service_info = self.services[service_id]
            service_info.last_heartbeat = datetime.utcnow()
            
            if status:
                service_info.status = status
            
            print(f"💓 Heartbeat received: {service_info.name}")
    
    async def discover_service(self, service_name: str) -> List[ServiceInfo]:
        """Discover service instances"""
        instances = []
        
        if service_name in self.service_instances:
            # Return healthy instances only
            for service_info in self.service_instances[service_name]:
                if self._is_service_healthy(service_info):
                    instances.append(service_info)
        
        print(f"🔍 Discovered {len(instances)} instances of {service_name}")
        return instances
    
    async def get_service_info(self, service_id: str) -> Optional[ServiceInfo]:
        """Get service information"""
        return self.services.get(service_id)
    
    async def list_services(self) -> Dict[str, List[ServiceInfo]]:
        """List all registered services"""
        result = {}
        
        for service_name, instances in self.service_instances.items():
            healthy_instances = [
                instance for instance in instances
                if self._is_service_healthy(instance)
            ]
            if healthy_instances:
                result[service_name] = healthy_instances
        
        return result
    
    def _is_service_healthy(self, service_info: ServiceInfo) -> bool:
        """Check if service is healthy based on heartbeat"""
        if service_info.status == ServiceStatus.STOPPED:
            return False
        
        time_since_heartbeat = datetime.utcnow() - service_info.last_heartbeat
        return time_since_heartbeat < self.heartbeat_timeout
    
    async def _cleanup_expired_services(self):
        """Clean up expired services"""
        while self._running:
            try:
                expired_services = []
                
                for service_id, service_info in self.services.items():
                    if not self._is_service_healthy(service_info):
                        expired_services.append(service_id)
                
                for service_id in expired_services:
                    await self.deregister_service(service_id)
                
                await asyncio.sleep(10)  # Cleanup every 10 seconds
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"⚠️ Cleanup error: {str(e)}")

class ServiceDiscoveryClient:
    """Client for service discovery"""
    
    def __init__(self, registry: ServiceRegistry):
        self.registry = registry
        self.service_cache: Dict[str, List[ServiceInfo]] = {}
        self.cache_ttl = timedelta(seconds=60)
        self.cache_timestamps: Dict[str, datetime] = {}
    
    async def find_service(self, service_name: str, use_cache: bool = True) -> Optional[ServiceInfo]:
        """Find a single healthy service instance"""
        instances = await self.find_services(service_name, use_cache)
        
        if not instances:
            return None
        
        # Simple load balancing - return random instance
        return random.choice(instances)
    
    async def find_services(self, service_name: str, use_cache: bool = True) -> List[ServiceInfo]:
        """Find all healthy service instances"""
        # Check cache first
        if use_cache and self._is_cache_valid(service_name):
            return self.service_cache[service_name]
        
        # Discover from registry
        instances = await self.registry.discover_service(service_name)
        
        # Update cache
        self.service_cache[service_name] = instances
        self.cache_timestamps[service_name] = datetime.utcnow()
        
        return instances
    
    def _is_cache_valid(self, service_name: str) -> bool:
        """Check if cache is valid"""
        if service_name not in self.cache_timestamps:
            return False
        
        age = datetime.utcnow() - self.cache_timestamps[service_name]
        return age < self.cache_ttl

class LoadBalancer:
    """Load balancer for service instances"""
    
    def __init__(self, discovery_client: ServiceDiscoveryClient):
        self.discovery_client = discovery_client
        self.algorithms = {
            "round_robin": self._round_robin,
            "random": self._random,
            "weighted": self._weighted,
            "least_connections": self._least_connections
        }
        self.round_robin_counters = defaultdict(int)
        self.connection_counts = defaultdict(int)
    
    async def get_service_instance(self, service_name: str, 
                                 algorithm: str = "round_robin") -> Optional[ServiceInfo]:
        """Get service instance using specified load balancing algorithm"""
        instances = await self.discovery_client.find_services(service_name)
        
        if not instances:
            return None
        
        if algorithm not in self.algorithms:
            algorithm = "round_robin"
        
        return self.algorithms[algorithm](service_name, instances)
    
    def _round_robin(self, service_name: str, instances: List[ServiceInfo]) -> ServiceInfo:
        """Round-robin load balancing"""
        counter = self.round_robin_counters[service_name]
        instance = instances[counter % len(instances)]
        self.round_robin_counters[service_name] = counter + 1
        return instance
    
    def _random(self, service_name: str, instances: List[ServiceInfo]) -> ServiceInfo:
        """Random load balancing"""
        return random.choice(instances)
    
    def _weighted(self, service_name: str, instances: List[ServiceInfo]) -> ServiceInfo:
        """Weighted load balancing based on service health"""
        # Simple weight based on status
        weights = []
        for instance in instances:
            if instance.status == ServiceStatus.HEALTHY:
                weights.append(3)
            elif instance.status == ServiceStatus.DEGRADED:
                weights.append(1)
            else:
                weights.append(0)
        
        # Weighted random selection
        if sum(weights) == 0:
            return random.choice(instances)
        
        return random.choices(instances, weights=weights)[0]
    
    def _least_connections(self, service_name: str, instances: List[ServiceInfo]) -> ServiceInfo:
        """Least connections load balancing"""
        # Find instance with least connections
        min_connections = float('inf')
        selected_instance = instances[0]
        
        for instance in instances:
            instance_key = f"{instance.host}:{instance.port}"
            connections = self.connection_counts[instance_key]
            
            if connections < min_connections:
                min_connections = connections
                selected_instance = instance
        
        return selected_instance
    
    def track_connection(self, service_info: ServiceInfo, increment: bool = True):
        """Track connection count for least connections algorithm"""
        instance_key = f"{service_info.host}:{service_info.port}"
        
        if increment:
            self.connection_counts[instance_key] += 1
        else:
            self.connection_counts[instance_key] = max(0, 
                self.connection_counts[instance_key] - 1)

# Service discovery demonstration
print("Service discovery örnekleri:")

async def service_discovery_demo():
    # Setup service registry
    registry = ServiceRegistry()
    await registry.start()
    
    # Setup discovery client and load balancer
    discovery_client = ServiceDiscoveryClient(registry)
    load_balancer = LoadBalancer(discovery_client)
    
    try:
        # Create and register services
        user_service1 = UserService()
        user_service1.port = 8001
        await user_service1.start()
        service_id1 = await registry.register_service(user_service1)
        
        user_service2 = UserService()
        user_service2.port = 8004
        await user_service2.start()
        service_id2 = await registry.register_service(user_service2)
        
        product_service = ProductService()
        await product_service.start()
        service_id3 = await registry.register_service(product_service)
        
        # Send heartbeats
        await registry.heartbeat(service_id1)
        await registry.heartbeat(service_id2)
        await registry.heartbeat(service_id3)
        
        # Discover services
        print("\n--- Service Discovery ---")
        user_instances = await discovery_client.find_services("user-service")
        print(f"Found {len(user_instances)} user service instances")
        
        # Load balancing tests
        print("\n--- Load Balancing ---")
        for algorithm in ["round_robin", "random", "weighted", "least_connections"]:
            print(f"\n{algorithm.title()} Algorithm:")
            for i in range(3):
                instance = await load_balancer.get_service_instance(
                    "user-service", algorithm
                )
                if instance:
                    print(f"  Request {i+1}: {instance.host}:{instance.port}")
        
        # List all services
        print("\n--- Service Listing ---")
        all_services = await registry.list_services()
        for service_name, instances in all_services.items():
            print(f"{service_name}: {len(instances)} instances")
        
        # Stop services
        await user_service1.stop()
        await user_service2.stop()
        await product_service.stop()
        
    finally:
        await registry.stop()

# Run service discovery demo
asyncio.run(service_discovery_demo())

# =============================================================================
# 3. MESSAGE QUEUE & EVENT HANDLING
# =============================================================================

print("\n=== Message Queue & Event Handling ===")

@dataclass
class Message:
    """Message structure"""
    id: str
    topic: str
    payload: Any
    headers: Dict[str, str]
    timestamp: datetime
    retry_count: int = 0
    max_retries: int = 3
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "topic": self.topic,
            "payload": self.payload,
            "headers": self.headers,
            "timestamp": self.timestamp.isoformat(),
            "retry_count": self.retry_count,
            "max_retries": self.max_retries
        }

class MessageBroker:
    """Simple message broker implementation"""
    
    def __init__(self):
        self.topics: Dict[str, List[Message]] = defaultdict(list)
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)
        self.dead_letter_queue: List[Message] = []
        self.running = False
        self._processing_task = None
    
    async def start(self):
        """Start message broker"""
        self.running = True
        self._processing_task = asyncio.create_task(self._process_messages())
        print("📬 Message broker started")
    
    async def stop(self):
        """Stop message broker"""
        self.running = False
        if self._processing_task:
            self._processing_task.cancel()
            try:
                await self._processing_task
            except asyncio.CancelledError:
                pass
        print("📬 Message broker stopped")
    
    async def publish(self, topic: str, payload: Any, headers: Dict[str, str] = None):
        """Publish message to topic"""
        message = Message(
            id=str(uuid.uuid4()),
            topic=topic,
            payload=payload,
            headers=headers or {},
            timestamp=datetime.utcnow()
        )
        
        self.topics[topic].append(message)
        print(f"📤 Message published to {topic}: {message.id}")
        
        return message.id
    
    def subscribe(self, topic: str, handler: Callable):
        """Subscribe to topic"""
        self.subscribers[topic].append(handler)
        print(f"📥 Subscribed to {topic}: {handler.__name__}")
    
    def unsubscribe(self, topic: str, handler: Callable):
        """Unsubscribe from topic"""
        if topic in self.subscribers and handler in self.subscribers[topic]:
            self.subscribers[topic].remove(handler)
            print(f"🚫 Unsubscribed from {topic}: {handler.__name__}")
    
    async def _process_messages(self):
        """Process messages in topics"""
        while self.running:
            try:
                for topic, messages in self.topics.items():
                    if messages and topic in self.subscribers:
                        message = messages.pop(0)  # FIFO
                        
                        for handler in self.subscribers[topic]:
                            try:
                                await self._handle_message(handler, message)
                            except Exception as e:
                                print(f"❌ Message handling error: {str(e)}")
                                await self._handle_failed_message(message, str(e))
                
                await asyncio.sleep(0.1)  # Process every 100ms
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                print(f"⚠️ Message processing error: {str(e)}")
    
    async def _handle_message(self, handler: Callable, message: Message):
        """Handle individual message"""
        print(f"🔄 Processing message {message.id} with {handler.__name__}")
        
        # Call handler
        if asyncio.iscoroutinefunction(handler):
            await handler(message)
        else:
            handler(message)
        
        print(f"✅ Message {message.id} processed successfully")
    
    async def _handle_failed_message(self, message: Message, error: str):
        """Handle failed message processing"""
        message.retry_count += 1
        
        if message.retry_count <= message.max_retries:
            # Retry message
            print(f"🔄 Retrying message {message.id} (attempt {message.retry_count})")
            self.topics[message.topic].append(message)
        else:
            # Send to dead letter queue
            print(f"☠️ Message {message.id} sent to dead letter queue")
            message.headers["error"] = error
            self.dead_letter_queue.append(message)

class EventStore:
    """Event store for event sourcing"""
    
    def __init__(self):
        self.events: Dict[str, List[dict]] = defaultdict(list)
        self.snapshots: Dict[str, dict] = {}
    
    async def append_event(self, aggregate_id: str, event_type: str, 
                          event_data: dict, version: int):
        """Append event to aggregate stream"""
        event = {
            "id": str(uuid.uuid4()),
            "aggregate_id": aggregate_id,
            "event_type": event_type,
            "event_data": event_data,
            "version": version,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.events[aggregate_id].append(event)
        print(f"📝 Event appended: {event_type} for {aggregate_id}")
        
        return event["id"]
    
    async def get_events(self, aggregate_id: str, from_version: int = 0) -> List[dict]:
        """Get events for aggregate from specific version"""
        events = self.events.get(aggregate_id, [])
        return [e for e in events if e["version"] >= from_version]
    
    async def save_snapshot(self, aggregate_id: str, snapshot_data: dict, version: int):
        """Save aggregate snapshot"""
        snapshot = {
            "aggregate_id": aggregate_id,
            "data": snapshot_data,
            "version": version,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        self.snapshots[aggregate_id] = snapshot
        print(f"📸 Snapshot saved for {aggregate_id} at version {version}")
    
    async def get_snapshot(self, aggregate_id: str) -> Optional[dict]:
        """Get latest snapshot for aggregate"""
        return self.snapshots.get(aggregate_id)

class EventHandler:
    """Base event handler"""
    
    def __init__(self, name: str):
        self.name = name
    
    async def handle(self, event: dict):
        """Handle event - override in subclasses"""
        print(f"🎯 {self.name} handling event: {event['event_type']}")

class UserEventHandler(EventHandler):
    """User-related event handler"""
    
    def __init__(self):
        super().__init__("UserEventHandler")
        self.user_projections = {}
    
    async def handle(self, event: dict):
        """Handle user events"""
        await super().handle(event)
        
        event_type = event["event_type"]
        aggregate_id = event["aggregate_id"]
        event_data = event["event_data"]
        
        if event_type == "UserCreated":
            self.user_projections[aggregate_id] = {
                "id": aggregate_id,
                "email": event_data["email"],
                "name": event_data["name"],
                "created_at": event["timestamp"]
            }
        elif event_type == "UserUpdated":
            if aggregate_id in self.user_projections:
                self.user_projections[aggregate_id].update(event_data)
        elif event_type == "UserDeleted":
            self.user_projections.pop(aggregate_id, None)

class OrderEventHandler(EventHandler):
    """Order-related event handler"""
    
    def __init__(self):
        super().__init__("OrderEventHandler")
        self.order_projections = {}
    
    async def handle(self, event: dict):
        """Handle order events"""
        await super().handle(event)
        
        event_type = event["event_type"]
        aggregate_id = event["aggregate_id"]
        event_data = event["event_data"]
        
        if event_type == "OrderCreated":
            self.order_projections[aggregate_id] = {
                "id": aggregate_id,
                "user_id": event_data["user_id"],
                "items": event_data["items"],
                "total": event_data["total"],
                "status": "created",
                "created_at": event["timestamp"]
            }
        elif event_type == "OrderStatusChanged":
            if aggregate_id in self.order_projections:
                self.order_projections[aggregate_id]["status"] = event_data["status"]

# Message queue demonstration
print("Message queue & event handling örnekleri:")

async def message_queue_demo():
    # Setup message broker
    broker = MessageBroker()
    await broker.start()
    
    # Setup event store
    event_store = EventStore()
    
    # Setup event handlers
    user_handler = UserEventHandler()
    order_handler = OrderEventHandler()
    
    try:
        # Define message handlers
        async def user_created_handler(message: Message):
            print(f"👤 New user created: {message.payload['email']}")
            
            # Store event
            await event_store.append_event(
                aggregate_id=message.payload["user_id"],
                event_type="UserCreated",
                event_data=message.payload,
                version=1
            )
            
            # Handle event
            event = {
                "aggregate_id": message.payload["user_id"],
                "event_type": "UserCreated",
                "event_data": message.payload,
                "timestamp": datetime.utcnow().isoformat()
            }
            await user_handler.handle(event)
        
        async def order_created_handler(message: Message):
            print(f"🛒 New order created: {message.payload['order_id']}")
            
            # Store event
            await event_store.append_event(
                aggregate_id=message.payload["order_id"],
                event_type="OrderCreated",
                event_data=message.payload,
                version=1
            )
            
            # Handle event
            event = {
                "aggregate_id": message.payload["order_id"],
                "event_type": "OrderCreated",
                "event_data": message.payload,
                "timestamp": datetime.utcnow().isoformat()
            }
            await order_handler.handle(event)
        
        async def notification_handler(message: Message):
            print(f"📧 Sending notification: {message.payload['type']}")
            # Simulate notification sending
            await asyncio.sleep(0.1)
        
        # Subscribe to topics
        broker.subscribe("user.created", user_created_handler)
        broker.subscribe("order.created", order_created_handler)
        broker.subscribe("notification.send", notification_handler)
        
        # Publish messages
        print("\n--- Publishing Messages ---")
        
        await broker.publish("user.created", {
            "user_id": "user_001",
            "email": "alice@example.com",
            "name": "Alice Johnson"
        })
        
        await broker.publish("order.created", {
            "order_id": "order_001",
            "user_id": "user_001",
            "items": [{"product_id": "prod_001", "quantity": 2}],
            "total": 59.98
        })
        
        await broker.publish("notification.send", {
            "type": "order_confirmation",
            "recipient": "alice@example.com",
            "order_id": "order_001"
        })
        
        # Wait for message processing
        await asyncio.sleep(1)
        
        # Check projections
        print("\n--- Event Projections ---")
        print(f"User projections: {user_handler.user_projections}")
        print(f"Order projections: {order_handler.order_projections}")
        
        # Get events from store
        print("\n--- Event Store ---")
        user_events = await event_store.get_events("user_001")
        order_events = await event_store.get_events("order_001")
        
        print(f"User events: {len(user_events)}")
        print(f"Order events: {len(order_events)}")
        
    finally:
        await broker.stop()

# Run message queue demo
asyncio.run(message_queue_demo())

print("\n" + "="*60)
print("MİKROSERVİS MİMARİSİ TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Microservice Foundations (BaseService, ServiceInfo)")
print("2. Service Discovery (Registry, Client, Load Balancer)")
print("3. Message Queue & Event Handling")
print("4. Event Store & Event Sourcing")
print("5. Health Checks & Service Monitoring")
print("6. Load Balancing Algorithms")

print("\nBir sonraki dosya: veritabani_islemleri.py")