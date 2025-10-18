"""
Python Deployment & DevOps - Comprehensive Guide
Containerization, Orchestration, Monitoring, CI/CD, Infrastructure as Code

Bu dosyada modern deployment stratejileri, containerization, Kubernetes,
monitoring, logging, CI/CD pipelines ve Infrastructure as Code konuları incelenecek.
"""

import asyncio
import json
import yaml
import time
import os
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
import uuid
import hashlib
import base64
from collections import defaultdict
import threading
import tempfile

# =============================================================================
# 1. CONTAINERIZATION & DOCKER
# =============================================================================

print("=== Containerization & Docker ===")

class ContainerStatus(Enum):
    """Container status enumeration"""
    CREATED = "created"
    RUNNING = "running"
    STOPPED = "stopped"
    FAILED = "failed"
    RESTARTING = "restarting"

@dataclass
class DockerImage:
    """Docker image representation"""
    name: str
    tag: str = "latest"
    dockerfile_path: str = "."
    build_args: Dict[str, str] = field(default_factory=dict)
    labels: Dict[str, str] = field(default_factory=dict)
    
    @property
    def full_name(self) -> str:
        """Get full image name with tag"""
        return f"{self.name}:{self.tag}"

@dataclass
class Container:
    """Container representation"""
    id: str
    name: str
    image: str
    status: ContainerStatus
    ports: Dict[str, str] = field(default_factory=dict)
    environment: Dict[str, str] = field(default_factory=dict)
    volumes: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "status": self.status.value,
            "ports": self.ports,
            "environment": self.environment,
            "volumes": self.volumes,
            "created_at": self.created_at.isoformat()
        }

class DockerfileGenerator:
    """Generate Dockerfile for Python applications"""
    
    def __init__(self, python_version: str = "3.11"):
        self.python_version = python_version
        self.instructions = []
    
    def generate_python_dockerfile(self, app_type: str = "web", 
                                 requirements_file: str = "requirements.txt",
                                 app_module: str = "app.main:app") -> str:
        """Generate Dockerfile for Python application"""
        
        # Base configurations for different app types
        configs = {
            "web": {
                "port": 8000,
                "cmd": f"uvicorn {app_module} --host 0.0.0.0 --port 8000"
            },
            "api": {
                "port": 8000,
                "cmd": f"uvicorn {app_module} --host 0.0.0.0 --port 8000"
            },
            "worker": {
                "port": None,
                "cmd": f"python -m {app_module}"
            },
            "cli": {
                "port": None,
                "cmd": f"python {app_module}"
            }
        }
        
        config = configs.get(app_type, configs["web"])
        
        dockerfile_content = f"""# Multi-stage build for Python {app_type}
FROM python:{self.python_version}-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PIP_NO_CACHE_DIR=1 \\
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        build-essential \\
        curl \\
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY {requirements_file} .
RUN pip install --upgrade pip \\
    && pip install -r {requirements_file}

# Production stage
FROM python:{self.python_version}-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PATH="/opt/venv/bin:$PATH"

# Install runtime dependencies
RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        curl \\
    && rm -rf /var/lib/apt/lists/* \\
    && groupadd -r appuser \\
    && useradd -r -g appuser appuser

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:{config['port'] or 8000}/health || exit 1
"""

        if config['port']:
            dockerfile_content += f"\n# Expose port\nEXPOSE {config['port']}\n"
        
        dockerfile_content += f"\n# Run application\nCMD [{', '.join(repr(part) for part in config['cmd'].split())}]"
        
        return dockerfile_content
    
    def generate_docker_compose(self, services: Dict[str, Dict]) -> str:
        """Generate docker-compose.yml"""
        
        compose_structure = {
            "version": "3.8",
            "services": {},
            "networks": {
                "app-network": {
                    "driver": "bridge"
                }
            },
            "volumes": {}
        }
        
        for service_name, config in services.items():
            service_def = {
                "build": config.get("build", "."),
                "ports": config.get("ports", []),
                "environment": config.get("environment", {}),
                "volumes": config.get("volumes", []),
                "depends_on": config.get("depends_on", []),
                "networks": ["app-network"]
            }
            
            # Add health check if specified
            if "healthcheck" in config:
                service_def["healthcheck"] = config["healthcheck"]
            
            # Add restart policy
            service_def["restart"] = config.get("restart", "unless-stopped")
            
            compose_structure["services"][service_name] = service_def
        
        return yaml.dump(compose_structure, default_flow_style=False)

class ContainerManager:
    """Mock container manager (simulates Docker operations)"""
    
    def __init__(self):
        self.containers: Dict[str, Container] = {}
        self.images: Dict[str, DockerImage] = {}
        self.networks: Dict[str, dict] = {}
    
    async def build_image(self, image: DockerImage) -> bool:
        """Build Docker image"""
        print(f"🔨 Building image: {image.full_name}")
        
        # Simulate build time
        await asyncio.sleep(2)
        
        self.images[image.full_name] = image
        print(f"✅ Image built successfully: {image.full_name}")
        
        return True
    
    async def run_container(self, name: str, image: str, 
                           ports: Dict[str, str] = None,
                           environment: Dict[str, str] = None,
                           volumes: List[str] = None) -> Container:
        """Run container"""
        
        if image not in self.images:
            raise ValueError(f"Image {image} not found")
        
        container_id = str(uuid.uuid4())[:12]
        
        container = Container(
            id=container_id,
            name=name,
            image=image,
            status=ContainerStatus.RUNNING,
            ports=ports or {},
            environment=environment or {},
            volumes=volumes or []
        )
        
        self.containers[container_id] = container
        
        print(f"🚀 Container started: {name} ({container_id})")
        return container
    
    async def stop_container(self, container_id: str) -> bool:
        """Stop container"""
        if container_id not in self.containers:
            return False
        
        self.containers[container_id].status = ContainerStatus.STOPPED
        print(f"🛑 Container stopped: {container_id}")
        return True
    
    async def remove_container(self, container_id: str) -> bool:
        """Remove container"""
        if container_id not in self.containers:
            return False
        
        del self.containers[container_id]
        print(f"🗑️ Container removed: {container_id}")
        return True
    
    def list_containers(self, all_containers: bool = False) -> List[Container]:
        """List containers"""
        if all_containers:
            return list(self.containers.values())
        else:
            return [c for c in self.containers.values() 
                   if c.status == ContainerStatus.RUNNING]
    
    def get_container_logs(self, container_id: str) -> str:
        """Get container logs (mock)"""
        if container_id not in self.containers:
            return ""
        
        # Mock logs
        container = self.containers[container_id]
        return f"""2024-01-01 10:00:01 INFO Starting {container.name}
2024-01-01 10:00:02 INFO Application initialized
2024-01-01 10:00:03 INFO Server listening on port 8000
2024-01-01 10:00:04 INFO Health check endpoint available
"""

# Containerization demonstration
print("Containerization örnekleri:")

async def containerization_demo():
    # Create Dockerfile generator
    dockerfile_gen = DockerfileGenerator()
    
    # Generate Dockerfile for web application
    web_dockerfile = dockerfile_gen.generate_python_dockerfile(
        app_type="web",
        app_module="app.main:app"
    )
    
    print("Generated Dockerfile for web application:")
    print("-" * 40)
    print(web_dockerfile[:500] + "..." if len(web_dockerfile) > 500 else web_dockerfile)
    
    # Generate docker-compose.yml
    services_config = {
        "web": {
            "build": ".",
            "ports": ["8000:8000"],
            "environment": {
                "DATABASE_URL": "postgresql://user:pass@db:5432/appdb",
                "REDIS_URL": "redis://redis:6379/0"
            },
            "depends_on": ["db", "redis"],
            "healthcheck": {
                "test": ["CMD", "curl", "-f", "http://localhost:8000/health"],
                "interval": "30s",
                "timeout": "10s",
                "retries": 3
            }
        },
        "db": {
            "build": False,
            "image": "postgres:15",
            "ports": ["5432:5432"],
            "environment": {
                "POSTGRES_DB": "appdb",
                "POSTGRES_USER": "user",
                "POSTGRES_PASSWORD": "pass"
            },
            "volumes": ["postgres_data:/var/lib/postgresql/data"]
        },
        "redis": {
            "build": False,
            "image": "redis:7-alpine",
            "ports": ["6379:6379"]
        }
    }
    
    docker_compose = dockerfile_gen.generate_docker_compose(services_config)
    
    print(f"\nGenerated docker-compose.yml:")
    print("-" * 40)
    print(docker_compose[:800] + "..." if len(docker_compose) > 800 else docker_compose)
    
    # Container management
    print(f"\n--- Container Management ---")
    
    container_manager = ContainerManager()
    
    # Build and run containers
    web_image = DockerImage(
        name="myapp/web",
        tag="v1.0.0",
        dockerfile_path="."
    )
    
    await container_manager.build_image(web_image)
    
    # Run web container
    web_container = await container_manager.run_container(
        name="web-app",
        image=web_image.full_name,
        ports={"8000": "8000"},
        environment={
            "DATABASE_URL": "postgresql://user:pass@localhost:5432/appdb",
            "DEBUG": "false"
        }
    )
    
    # List running containers
    running_containers = container_manager.list_containers()
    print(f"\nRunning containers: {len(running_containers)}")
    for container in running_containers:
        print(f"  - {container.name} ({container.id}) - {container.status.value}")
    
    # Get logs
    logs = container_manager.get_container_logs(web_container.id)
    print(f"\nContainer logs:\n{logs}")

# Run containerization demo
asyncio.run(containerization_demo())

# =============================================================================
# 2. KUBERNETES ORCHESTRATION
# =============================================================================

print("\n=== Kubernetes Orchestration ===")

class KubernetesManifestGenerator:
    """Generate Kubernetes manifests"""
    
    def __init__(self):
        self.api_version = "apps/v1"
    
    def generate_deployment(self, app_name: str, image: str, replicas: int = 3,
                           port: int = 8000, env_vars: Dict[str, str] = None) -> dict:
        """Generate Kubernetes Deployment manifest"""
        
        deployment = {
            "apiVersion": self.api_version,
            "kind": "Deployment",
            "metadata": {
                "name": f"{app_name}-deployment",
                "labels": {
                    "app": app_name,
                    "version": "v1"
                }
            },
            "spec": {
                "replicas": replicas,
                "selector": {
                    "matchLabels": {
                        "app": app_name
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "app": app_name,
                            "version": "v1"
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "name": app_name,
                                "image": image,
                                "ports": [
                                    {
                                        "containerPort": port,
                                        "name": "http"
                                    }
                                ],
                                "env": [
                                    {"name": k, "value": v} 
                                    for k, v in (env_vars or {}).items()
                                ],
                                "resources": {
                                    "requests": {
                                        "memory": "256Mi",
                                        "cpu": "250m"
                                    },
                                    "limits": {
                                        "memory": "512Mi",
                                        "cpu": "500m"
                                    }
                                },
                                "livenessProbe": {
                                    "httpGet": {
                                        "path": "/health",
                                        "port": port
                                    },
                                    "initialDelaySeconds": 30,
                                    "periodSeconds": 10
                                },
                                "readinessProbe": {
                                    "httpGet": {
                                        "path": "/ready",
                                        "port": port
                                    },
                                    "initialDelaySeconds": 5,
                                    "periodSeconds": 5
                                }
                            }
                        ]
                    }
                }
            }
        }
        
        return deployment
    
    def generate_service(self, app_name: str, port: int = 8000, 
                        target_port: int = 8000, service_type: str = "ClusterIP") -> dict:
        """Generate Kubernetes Service manifest"""
        
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": f"{app_name}-service",
                "labels": {
                    "app": app_name
                }
            },
            "spec": {
                "selector": {
                    "app": app_name
                },
                "ports": [
                    {
                        "port": port,
                        "targetPort": target_port,
                        "name": "http"
                    }
                ],
                "type": service_type
            }
        }
        
        return service
    
    def generate_configmap(self, app_name: str, config_data: Dict[str, str]) -> dict:
        """Generate Kubernetes ConfigMap manifest"""
        
        configmap = {
            "apiVersion": "v1",
            "kind": "ConfigMap",
            "metadata": {
                "name": f"{app_name}-config",
                "labels": {
                    "app": app_name
                }
            },
            "data": config_data
        }
        
        return configmap
    
    def generate_secret(self, app_name: str, secret_data: Dict[str, str]) -> dict:
        """Generate Kubernetes Secret manifest"""
        
        # Encode secret values to base64
        encoded_data = {}
        for key, value in secret_data.items():
            encoded_data[key] = base64.b64encode(value.encode()).decode()
        
        secret = {
            "apiVersion": "v1",
            "kind": "Secret",
            "metadata": {
                "name": f"{app_name}-secret",
                "labels": {
                    "app": app_name
                }
            },
            "type": "Opaque",
            "data": encoded_data
        }
        
        return secret
    
    def generate_ingress(self, app_name: str, host: str, 
                        service_port: int = 80, tls: bool = False) -> dict:
        """Generate Kubernetes Ingress manifest"""
        
        ingress = {
            "apiVersion": "networking.k8s.io/v1",
            "kind": "Ingress",
            "metadata": {
                "name": f"{app_name}-ingress",
                "labels": {
                    "app": app_name
                },
                "annotations": {
                    "kubernetes.io/ingress.class": "nginx",
                    "nginx.ingress.kubernetes.io/rewrite-target": "/"
                }
            },
            "spec": {
                "rules": [
                    {
                        "host": host,
                        "http": {
                            "paths": [
                                {
                                    "path": "/",
                                    "pathType": "Prefix",
                                    "backend": {
                                        "service": {
                                            "name": f"{app_name}-service",
                                            "port": {
                                                "number": service_port
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
        if tls:
            ingress["spec"]["tls"] = [
                {
                    "hosts": [host],
                    "secretName": f"{app_name}-tls"
                }
            ]
        
        return ingress
    
    def generate_hpa(self, app_name: str, min_replicas: int = 3, 
                    max_replicas: int = 10, cpu_threshold: int = 70) -> dict:
        """Generate Horizontal Pod Autoscaler manifest"""
        
        hpa = {
            "apiVersion": "autoscaling/v2",
            "kind": "HorizontalPodAutoscaler",
            "metadata": {
                "name": f"{app_name}-hpa",
                "labels": {
                    "app": app_name
                }
            },
            "spec": {
                "scaleTargetRef": {
                    "apiVersion": "apps/v1",
                    "kind": "Deployment",
                    "name": f"{app_name}-deployment"
                },
                "minReplicas": min_replicas,
                "maxReplicas": max_replicas,
                "metrics": [
                    {
                        "type": "Resource",
                        "resource": {
                            "name": "cpu",
                            "target": {
                                "type": "Utilization",
                                "averageUtilization": cpu_threshold
                            }
                        }
                    }
                ]
            }
        }
        
        return hpa

class KubernetesCluster:
    """Mock Kubernetes cluster (simulates kubectl operations)"""
    
    def __init__(self):
        self.resources: Dict[str, Dict[str, Any]] = defaultdict(dict)
        self.pods: Dict[str, dict] = {}
        self.namespaces = {"default"}
    
    async def apply_manifest(self, manifest: dict, namespace: str = "default") -> bool:
        """Apply Kubernetes manifest"""
        kind = manifest["kind"]
        name = manifest["metadata"]["name"]
        
        print(f"🚀 Applying {kind}: {name}")
        
        # Simulate apply time
        await asyncio.sleep(0.5)
        
        # Store resource
        resource_key = f"{kind.lower()}s"
        self.resources[resource_key][name] = manifest
        
        # If it's a deployment, create mock pods
        if kind == "Deployment":
            await self._create_pods_for_deployment(manifest, namespace)
        
        print(f"✅ {kind} {name} applied successfully")
        return True
    
    async def _create_pods_for_deployment(self, deployment: dict, namespace: str):
        """Create mock pods for deployment"""
        replicas = deployment["spec"]["replicas"]
        app_name = deployment["metadata"]["labels"]["app"]
        
        for i in range(replicas):
            pod_name = f"{app_name}-{uuid.uuid4().hex[:8]}"
            
            pod = {
                "name": pod_name,
                "namespace": namespace,
                "status": "Running",
                "app": app_name,
                "created_at": datetime.utcnow().isoformat()
            }
            
            self.pods[pod_name] = pod
    
    def get_pods(self, namespace: str = "default", label_selector: str = None) -> List[dict]:
        """Get pods"""
        pods = list(self.pods.values())
        
        if label_selector:
            # Simple label filtering
            app_name = label_selector.split("=")[1] if "=" in label_selector else None
            if app_name:
                pods = [p for p in pods if p.get("app") == app_name]
        
        return pods
    
    def get_resource(self, kind: str, name: str) -> Optional[dict]:
        """Get resource by kind and name"""
        resource_key = f"{kind.lower()}s"
        return self.resources[resource_key].get(name)
    
    def list_resources(self, kind: str) -> List[dict]:
        """List resources by kind"""
        resource_key = f"{kind.lower()}s"
        return list(self.resources[resource_key].values())
    
    async def scale_deployment(self, name: str, replicas: int) -> bool:
        """Scale deployment"""
        deployment = self.get_resource("Deployment", name)
        if not deployment:
            return False
        
        print(f"📈 Scaling deployment {name} to {replicas} replicas")
        deployment["spec"]["replicas"] = replicas
        
        # Update pods
        app_name = deployment["metadata"]["labels"]["app"]
        current_pods = [p for p in self.pods.values() if p.get("app") == app_name]
        
        if len(current_pods) < replicas:
            # Add pods
            for i in range(replicas - len(current_pods)):
                pod_name = f"{app_name}-{uuid.uuid4().hex[:8]}"
                pod = {
                    "name": pod_name,
                    "namespace": "default",
                    "status": "Running", 
                    "app": app_name,
                    "created_at": datetime.utcnow().isoformat()
                }
                self.pods[pod_name] = pod
        
        elif len(current_pods) > replicas:
            # Remove excess pods
            pods_to_remove = current_pods[replicas:]
            for pod in pods_to_remove:
                del self.pods[pod["name"]]
        
        print(f"✅ Deployment {name} scaled successfully")
        return True
    
    def get_cluster_status(self) -> dict:
        """Get cluster status"""
        total_pods = len(self.pods)
        running_pods = sum(1 for p in self.pods.values() if p["status"] == "Running")
        
        return {
            "total_pods": total_pods,
            "running_pods": running_pods,
            "deployments": len(self.resources["deployments"]),
            "services": len(self.resources["services"]),
            "configmaps": len(self.resources["configmaps"]),
            "secrets": len(self.resources["secrets"])
        }

# Kubernetes demonstration
print("Kubernetes orchestration örnekleri:")

async def kubernetes_demo():
    # Create manifest generator
    k8s_gen = KubernetesManifestGenerator()
    
    # Generate manifests for web application
    app_name = "python-web-app"
    
    # 1. Deployment
    deployment = k8s_gen.generate_deployment(
        app_name=app_name,
        image="myapp/web:v1.0.0",
        replicas=3,
        port=8000,
        env_vars={
            "DATABASE_URL": "postgresql://user:pass@db:5432/appdb",
            "DEBUG": "false",
            "LOG_LEVEL": "INFO"
        }
    )
    
    print("Generated Kubernetes Deployment:")
    print(yaml.dump(deployment, default_flow_style=False)[:600] + "...")
    
    # 2. Service
    service = k8s_gen.generate_service(
        app_name=app_name,
        port=80,
        target_port=8000,
        service_type="ClusterIP"
    )
    
    # 3. ConfigMap
    configmap = k8s_gen.generate_configmap(
        app_name=app_name,
        config_data={
            "app.yaml": """
app:
  name: python-web-app
  version: v1.0.0
  environment: production

database:
  pool_size: 10
  timeout: 30

redis:
  max_connections: 100
"""
        }
    )
    
    # 4. Secret
    secret = k8s_gen.generate_secret(
        app_name=app_name,
        secret_data={
            "DATABASE_PASSWORD": "super_secret_password",
            "SECRET_KEY": "jwt_secret_key_12345"
        }
    )
    
    # 5. Ingress
    ingress = k8s_gen.generate_ingress(
        app_name=app_name,
        host="myapp.example.com",
        service_port=80,
        tls=True
    )
    
    # 6. HPA
    hpa = k8s_gen.generate_hpa(
        app_name=app_name,
        min_replicas=3,
        max_replicas=10,
        cpu_threshold=70
    )
    
    print(f"\nGenerated {len([deployment, service, configmap, secret, ingress, hpa])} Kubernetes manifests")
    
    # Simulate cluster operations
    print(f"\n--- Cluster Operations ---")
    
    cluster = KubernetesCluster()
    
    # Apply manifests
    await cluster.apply_manifest(deployment)
    await cluster.apply_manifest(service)
    await cluster.apply_manifest(configmap)
    await cluster.apply_manifest(secret)
    await cluster.apply_manifest(ingress)
    await cluster.apply_manifest(hpa)
    
    # Check cluster status
    status = cluster.get_cluster_status()
    print(f"\nCluster Status:")
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    # List pods
    pods = cluster.get_pods(label_selector=f"app={app_name}")
    print(f"\nPods for {app_name}:")
    for pod in pods:
        print(f"  - {pod['name']}: {pod['status']}")
    
    # Scale deployment
    await cluster.scale_deployment(f"{app_name}-deployment", 5)
    
    # Check pods after scaling
    pods = cluster.get_pods(label_selector=f"app={app_name}")
    print(f"\nPods after scaling:")
    for pod in pods:
        print(f"  - {pod['name']}: {pod['status']}")

# Run Kubernetes demo
asyncio.run(kubernetes_demo())

# =============================================================================
# 3. MONITORING & OBSERVABILITY
# =============================================================================

print("\n=== Monitoring & Observability ===")

@dataclass
class MetricPoint:
    """Metric data point"""
    name: str
    value: float
    timestamp: datetime
    labels: Dict[str, str] = field(default_factory=dict)
    
    def to_prometheus_format(self) -> str:
        """Convert to Prometheus format"""
        labels_str = ""
        if self.labels:
            label_pairs = [f'{k}="{v}"' for k, v in self.labels.items()]
            labels_str = "{" + ",".join(label_pairs) + "}"
        
        return f"{self.name}{labels_str} {self.value}"

class MetricsCollector:
    """Application metrics collector"""
    
    def __init__(self):
        self.metrics: Dict[str, List[MetricPoint]] = defaultdict(list)
        self.counters: Dict[str, float] = defaultdict(float)
        self.gauges: Dict[str, float] = {}
        self.histograms: Dict[str, List[float]] = defaultdict(list)
    
    def counter(self, name: str, value: float = 1, labels: Dict[str, str] = None):
        """Increment counter metric"""
        self.counters[name] += value
        
        metric = MetricPoint(
            name=name,
            value=self.counters[name],
            timestamp=datetime.utcnow(),
            labels=labels or {}
        )
        
        self.metrics[name].append(metric)
    
    def gauge(self, name: str, value: float, labels: Dict[str, str] = None):
        """Set gauge metric"""
        self.gauges[name] = value
        
        metric = MetricPoint(
            name=name,
            value=value,
            timestamp=datetime.utcnow(),
            labels=labels or {}
        )
        
        self.metrics[name].append(metric)
    
    def histogram(self, name: str, value: float, labels: Dict[str, str] = None):
        """Record histogram metric"""
        self.histograms[name].append(value)
        
        metric = MetricPoint(
            name=name,
            value=value,
            timestamp=datetime.utcnow(),
            labels=labels or {}
        )
        
        self.metrics[name].append(metric)
    
    def get_prometheus_metrics(self) -> str:
        """Export metrics in Prometheus format"""
        output = []
        
        # Counters
        for name, value in self.counters.items():
            output.append(f"# TYPE {name} counter")
            output.append(f"{name} {value}")
        
        # Gauges
        for name, value in self.gauges.items():
            output.append(f"# TYPE {name} gauge")
            output.append(f"{name} {value}")
        
        # Histograms (simplified)
        for name, values in self.histograms.items():
            if values:
                output.append(f"# TYPE {name} histogram")
                output.append(f"{name}_count {len(values)}")
                output.append(f"{name}_sum {sum(values)}")
                
                # Calculate quantiles
                sorted_values = sorted(values)
                for quantile in [0.5, 0.95, 0.99]:
                    idx = int(len(sorted_values) * quantile)
                    if idx < len(sorted_values):
                        value = sorted_values[idx]
                        output.append(f'{name}_bucket{{le="{quantile}"}} {value}')
        
        return "\n".join(output)
    
    def get_metrics_summary(self) -> dict:
        """Get metrics summary"""
        return {
            "counters": dict(self.counters),
            "gauges": dict(self.gauges),
            "histograms": {
                name: {
                    "count": len(values),
                    "sum": sum(values),
                    "avg": sum(values) / len(values) if values else 0,
                    "min": min(values) if values else 0,
                    "max": max(values) if values else 0
                }
                for name, values in self.histograms.items()
            }
        }

class LogLevel(Enum):
    """Log levels"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@dataclass
class LogEntry:
    """Structured log entry"""
    level: LogLevel
    message: str
    timestamp: datetime
    logger_name: str
    module: str = ""
    function: str = ""
    line: int = 0
    extra: Dict[str, Any] = field(default_factory=dict)
    
    def to_json(self) -> str:
        """Convert to JSON format"""
        return json.dumps({
            "timestamp": self.timestamp.isoformat(),
            "level": self.level.value,
            "logger": self.logger_name,
            "message": self.message,
            "module": self.module,
            "function": self.function,
            "line": self.line,
            **self.extra
        })

class StructuredLogger:
    """Structured logger with multiple outputs"""
    
    def __init__(self, name: str):
        self.name = name
        self.handlers = []
        self.min_level = LogLevel.INFO
    
    def add_handler(self, handler: Callable[[LogEntry], None]):
        """Add log handler"""
        self.handlers.append(handler)
    
    def set_level(self, level: LogLevel):
        """Set minimum log level"""
        self.min_level = level
    
    def _log(self, level: LogLevel, message: str, **kwargs):
        """Internal logging method"""
        if self._should_log(level):
            entry = LogEntry(
                level=level,
                message=message,
                timestamp=datetime.utcnow(),
                logger_name=self.name,
                extra=kwargs
            )
            
            for handler in self.handlers:
                handler(entry)
    
    def _should_log(self, level: LogLevel) -> bool:
        """Check if should log at given level"""
        levels = [LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARNING, LogLevel.ERROR, LogLevel.CRITICAL]
        return levels.index(level) >= levels.index(self.min_level)
    
    def debug(self, message: str, **kwargs):
        """Log debug message"""
        self._log(LogLevel.DEBUG, message, **kwargs)
    
    def info(self, message: str, **kwargs):
        """Log info message"""
        self._log(LogLevel.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs):
        """Log warning message"""
        self._log(LogLevel.WARNING, message, **kwargs)
    
    def error(self, message: str, **kwargs):
        """Log error message"""
        self._log(LogLevel.ERROR, message, **kwargs)
    
    def critical(self, message: str, **kwargs):
        """Log critical message"""
        self._log(LogLevel.CRITICAL, message, **kwargs)

class MonitoringDashboard:
    """Monitoring dashboard for visualizing metrics"""
    
    def __init__(self, metrics_collector: MetricsCollector):
        self.metrics_collector = metrics_collector
        self.alerts = []
    
    def create_alert(self, name: str, metric_name: str, 
                    threshold: float, condition: str = "greater_than"):
        """Create alert rule"""
        alert = {
            "name": name,
            "metric_name": metric_name,
            "threshold": threshold,
            "condition": condition,
            "created_at": datetime.utcnow()
        }
        
        self.alerts.append(alert)
        print(f"🚨 Alert created: {name} - {metric_name} {condition} {threshold}")
    
    def check_alerts(self) -> List[dict]:
        """Check alert conditions"""
        triggered_alerts = []
        
        for alert in self.alerts:
            metric_name = alert["metric_name"]
            
            # Get latest metric value
            latest_value = None
            if metric_name in self.metrics_collector.counters:
                latest_value = self.metrics_collector.counters[metric_name]
            elif metric_name in self.metrics_collector.gauges:
                latest_value = self.metrics_collector.gauges[metric_name]
            
            if latest_value is not None:
                condition_met = False
                
                if alert["condition"] == "greater_than":
                    condition_met = latest_value > alert["threshold"]
                elif alert["condition"] == "less_than":
                    condition_met = latest_value < alert["threshold"]
                elif alert["condition"] == "equals":
                    condition_met = latest_value == alert["threshold"]
                
                if condition_met:
                    triggered_alert = {
                        **alert,
                        "current_value": latest_value,
                        "triggered_at": datetime.utcnow()
                    }
                    triggered_alerts.append(triggered_alert)
        
        return triggered_alerts
    
    def get_dashboard_data(self) -> dict:
        """Get dashboard data"""
        metrics_summary = self.metrics_collector.get_metrics_summary()
        triggered_alerts = self.check_alerts()
        
        return {
            "metrics": metrics_summary,
            "alerts": {
                "total": len(self.alerts),
                "triggered": len(triggered_alerts),
                "details": triggered_alerts
            },
            "system_health": self._calculate_system_health(metrics_summary)
        }
    
    def _calculate_system_health(self, metrics: dict) -> dict:
        """Calculate overall system health score"""
        health_score = 100
        issues = []
        
        # Check error rates
        if "http_requests_total" in metrics["counters"] and "http_errors_total" in metrics["counters"]:
            total_requests = metrics["counters"]["http_requests_total"]
            total_errors = metrics["counters"]["http_errors_total"]
            
            if total_requests > 0:
                error_rate = (total_errors / total_requests) * 100
                if error_rate > 5:  # More than 5% error rate
                    health_score -= 20
                    issues.append(f"High error rate: {error_rate:.1f}%")
        
        # Check response times
        if "http_request_duration" in metrics["histograms"]:
            duration_stats = metrics["histograms"]["http_request_duration"]
            if duration_stats["avg"] > 1.0:  # More than 1 second average
                health_score -= 15
                issues.append(f"Slow response time: {duration_stats['avg']:.2f}s")
        
        # Check memory usage
        if "memory_usage_percent" in metrics["gauges"]:
            memory_usage = metrics["gauges"]["memory_usage_percent"]
            if memory_usage > 80:  # More than 80% memory usage
                health_score -= 25
                issues.append(f"High memory usage: {memory_usage:.1f}%")
        
        health_status = "healthy"
        if health_score < 70:
            health_status = "critical"
        elif health_score < 85:
            health_status = "warning"
        
        return {
            "score": max(0, health_score),
            "status": health_status,
            "issues": issues
        }

# =============================================================================
# 4. CI/CD PIPELINE
# =============================================================================

print("\n=== CI/CD Pipeline ===")

class PipelineStage(Enum):
    """Pipeline stage types"""
    BUILD = "build"
    TEST = "test"
    SECURITY = "security"
    DEPLOY = "deploy"
    VERIFY = "verify"

@dataclass
class PipelineStep:
    """Pipeline step definition"""
    name: str
    stage: PipelineStage
    script: List[str]
    depends_on: List[str] = field(default_factory=list)
    environment: Dict[str, str] = field(default_factory=dict)
    timeout: int = 300  # 5 minutes default
    retry_count: int = 0
    
@dataclass
class PipelineExecution:
    """Pipeline execution result"""
    step_name: str
    status: str  # success, failed, skipped
    start_time: datetime
    end_time: datetime
    output: str
    exit_code: int = 0
    
    @property
    def duration(self) -> timedelta:
        """Get execution duration"""
        return self.end_time - self.start_time

class GitOpsRepository:
    """GitOps repository simulation"""
    
    def __init__(self):
        self.branches = {"main": []}
        self.commits = {}
        self.current_branch = "main"
    
    def commit(self, message: str, files: Dict[str, str]) -> str:
        """Create commit"""
        commit_id = hashlib.sha1(f"{message}{time.time()}".encode()).hexdigest()[:8]
        
        commit = {
            "id": commit_id,
            "message": message,
            "files": files,
            "timestamp": datetime.utcnow(),
            "author": "ci-system",
            "branch": self.current_branch
        }
        
        self.commits[commit_id] = commit
        self.branches[self.current_branch].append(commit_id)
        
        print(f"📝 Commit created: {commit_id} - {message}")
        return commit_id
    
    def get_latest_commit(self, branch: str = None) -> Optional[dict]:
        """Get latest commit"""
        branch = branch or self.current_branch
        
        if branch in self.branches and self.branches[branch]:
            latest_commit_id = self.branches[branch][-1]
            return self.commits[latest_commit_id]
        
        return None
    
    def create_tag(self, name: str, commit_id: str) -> bool:
        """Create git tag"""
        if commit_id in self.commits:
            print(f"🏷️ Tag created: {name} -> {commit_id}")
            return True
        return False

class CICDPipeline:
    """CI/CD Pipeline implementation"""
    
    def __init__(self, repository: GitOpsRepository):
        self.repository = repository
        self.steps: List[PipelineStep] = []
        self.executions: List[PipelineExecution] = []
        self.environment_vars = {}
        self.secrets = {}
    
    def add_step(self, step: PipelineStep):
        """Add pipeline step"""
        self.steps.append(step)
        print(f"🔧 Pipeline step added: {step.name} ({step.stage.value})")
    
    def set_environment(self, env_vars: Dict[str, str]):
        """Set environment variables"""
        self.environment_vars.update(env_vars)
    
    def set_secrets(self, secrets: Dict[str, str]):
        """Set secrets"""
        self.secrets.update(secrets)
    
    async def run_pipeline(self, commit_id: str) -> Dict[str, Any]:
        """Run complete pipeline"""
        print(f"\n🚀 Starting CI/CD Pipeline for commit: {commit_id}")
        print(f"{'='*60}")
        
        commit = self.repository.commits.get(commit_id)
        if not commit:
            return {"error": "Commit not found"}
        
        pipeline_start = datetime.utcnow()
        results = {"commit": commit_id, "steps": [], "overall_status": "success"}
        
        # Group steps by stage
        stages = defaultdict(list)
        for step in self.steps:
            stages[step.stage].append(step)
        
        # Execute stages in order
        stage_order = [PipelineStage.BUILD, PipelineStage.TEST, 
                      PipelineStage.SECURITY, PipelineStage.DEPLOY, 
                      PipelineStage.VERIFY]
        
        for stage in stage_order:
            if stage not in stages:
                continue
            
            print(f"\n📋 Stage: {stage.value.upper()}")
            print(f"{'-'*40}")
            
            # Execute all steps in current stage
            stage_success = True
            for step in stages[stage]:
                execution = await self._execute_step(step, commit)
                results["steps"].append(execution)
                
                if execution.status != "success":
                    stage_success = False
                    results["overall_status"] = "failed"
                    break
            
            # Stop pipeline if stage failed
            if not stage_success:
                break
        
        pipeline_end = datetime.utcnow()
        results["duration"] = (pipeline_end - pipeline_start).total_seconds()
        
        self._print_pipeline_summary(results)
        
        return results
    
    async def _execute_step(self, step: PipelineStep, commit: dict) -> dict:
        """Execute individual pipeline step"""
        print(f"🔄 Executing: {step.name}")
        
        start_time = datetime.utcnow()
        
        # Simulate step execution
        try:
            # Combine environment variables
            env = {**self.environment_vars, **step.environment}
            
            # Execute scripts (simulated)
            output_lines = []
            exit_code = 0
            
            for script_line in step.script:
                # Simulate script execution
                await asyncio.sleep(0.1)  # Simulate execution time
                
                output_lines.append(f"$ {script_line}")
                
                # Simulate different script outcomes
                if "test" in script_line.lower():
                    if "pytest" in script_line:
                        output_lines.append("===== test session starts =====")
                        output_lines.append("collected 15 items")
                        output_lines.append("test_api.py ............... [100%]")
                        output_lines.append("===== 15 passed in 2.34s =====")
                    else:
                        output_lines.append("All tests passed")
                
                elif "build" in script_line.lower():
                    output_lines.append("Building application...")
                    output_lines.append("Successfully built application")
                
                elif "deploy" in script_line.lower():
                    output_lines.append("Deploying to production...")
                    output_lines.append("Deployment successful")
                
                elif "security" in script_line.lower():
                    output_lines.append("Running security scan...")
                    output_lines.append("No vulnerabilities found")
                
                else:
                    output_lines.append("Command executed successfully")
            
            status = "success"
            
        except Exception as e:
            output_lines.append(f"Error: {str(e)}")
            exit_code = 1
            status = "failed"
        
        end_time = datetime.utcnow()
        duration = end_time - start_time
        
        execution = {
            "step_name": step.name,
            "stage": step.stage.value,
            "status": status,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration": duration.total_seconds(),
            "output": "\n".join(output_lines),
            "exit_code": exit_code
        }
        
        status_icon = "✅" if status == "success" else "❌"
        print(f"{status_icon} {step.name} ({duration.total_seconds():.2f}s)")
        
        return execution
    
    def _print_pipeline_summary(self, results: dict):
        """Print pipeline execution summary"""
        print(f"\n🏁 Pipeline Summary")
        print(f"{'='*60}")
        print(f"Commit: {results['commit']}")
        print(f"Overall Status: {results['overall_status'].upper()}")
        print(f"Duration: {results['duration']:.2f}s")
        
        print(f"\nStep Results:")
        for step in results["steps"]:
            status_icon = "✅" if step["status"] == "success" else "❌"
            print(f"{status_icon} {step['step_name']} ({step['stage']}) - {step['duration']:.2f}s")

# =============================================================================
# 5. INFRASTRUCTURE AS CODE
# =============================================================================

print("\n=== Infrastructure as Code ===")

class TerraformResource:
    """Terraform resource definition"""
    
    def __init__(self, resource_type: str, name: str, **kwargs):
        self.resource_type = resource_type
        self.name = name
        self.attributes = kwargs
    
    def to_hcl(self) -> str:
        """Convert to HCL format"""
        lines = [f'resource "{self.resource_type}" "{self.name}" {{']
        
        for key, value in self.attributes.items():
            if isinstance(value, str):
                lines.append(f'  {key} = "{value}"')
            elif isinstance(value, bool):
                lines.append(f'  {key} = {str(value).lower()}')
            elif isinstance(value, (int, float)):
                lines.append(f'  {key} = {value}')
            elif isinstance(value, list):
                formatted_list = ", ".join(f'"{item}"' if isinstance(item, str) else str(item) for item in value)
                lines.append(f'  {key} = [{formatted_list}]')
            elif isinstance(value, dict):
                lines.append(f'  {key} = {{')
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, str):
                        lines.append(f'    {sub_key} = "{sub_value}"')
                    else:
                        lines.append(f'    {sub_key} = {sub_value}')
                lines.append(f'  }}')
        
        lines.append('}')
        return '\n'.join(lines)

class InfrastructureTemplate:
    """Infrastructure as Code template generator"""
    
    def __init__(self):
        self.resources = []
        self.variables = {}
        self.outputs = {}
    
    def add_resource(self, resource: TerraformResource):
        """Add resource to template"""
        self.resources.append(resource)
    
    def add_variable(self, name: str, type_name: str, description: str, default=None):
        """Add variable definition"""
        var_def = {
            "type": type_name,
            "description": description
        }
        if default is not None:
            var_def["default"] = default
        
        self.variables[name] = var_def
    
    def add_output(self, name: str, value: str, description: str = ""):
        """Add output definition"""
        self.outputs[name] = {
            "value": value,
            "description": description
        }
    
    def generate_terraform(self) -> str:
        """Generate complete Terraform configuration"""
        lines = []
        
        # Provider configuration
        lines.append('terraform {')
        lines.append('  required_providers {')
        lines.append('    aws = {')
        lines.append('      source  = "hashicorp/aws"')
        lines.append('      version = "~> 5.0"')
        lines.append('    }')
        lines.append('  }')
        lines.append('}')
        lines.append('')
        
        lines.append('provider "aws" {')
        lines.append('  region = var.aws_region')
        lines.append('}')
        lines.append('')
        
        # Variables
        if self.variables:
            for name, var_def in self.variables.items():
                lines.append(f'variable "{name}" {{')
                lines.append(f'  type        = {var_def["type"]}')
                lines.append(f'  description = "{var_def["description"]}"')
                if "default" in var_def:
                    if isinstance(var_def["default"], str):
                        lines.append(f'  default     = "{var_def["default"]}"')
                    else:
                        lines.append(f'  default     = {var_def["default"]}')
                lines.append('}')
                lines.append('')
        
        # Resources
        for resource in self.resources:
            lines.append(resource.to_hcl())
            lines.append('')
        
        # Outputs
        if self.outputs:
            for name, output_def in self.outputs.items():
                lines.append(f'output "{name}" {{')
                lines.append(f'  value       = {output_def["value"]}')
                if output_def["description"]:
                    lines.append(f'  description = "{output_def["description"]}"')
                lines.append('}')
                lines.append('')
        
        return '\n'.join(lines)
    
    def create_web_application_infrastructure(self, app_name: str):
        """Create infrastructure for web application"""
        
        # Add variables
        self.add_variable("aws_region", "string", "AWS region", "us-west-2")
        self.add_variable("app_name", "string", "Application name", app_name)
        self.add_variable("environment", "string", "Environment", "production")
        
        # VPC
        vpc = TerraformResource(
            "aws_vpc", "main",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            tags={"Name": f"{app_name}-vpc", "Environment": "var.environment"}
        )
        self.add_resource(vpc)
        
        # Subnets
        public_subnet = TerraformResource(
            "aws_subnet", "public",
            vpc_id="aws_vpc.main.id",
            cidr_block="10.0.1.0/24",
            availability_zone="data.aws_availability_zones.available.names[0]",
            map_public_ip_on_launch=True,
            tags={"Name": f"{app_name}-public-subnet"}
        )
        self.add_resource(public_subnet)
        
        private_subnet = TerraformResource(
            "aws_subnet", "private",
            vpc_id="aws_vpc.main.id",
            cidr_block="10.0.2.0/24",
            availability_zone="data.aws_availability_zones.available.names[1]",
            tags={"Name": f"{app_name}-private-subnet"}
        )
        self.add_resource(private_subnet)
        
        # Internet Gateway
        igw = TerraformResource(
            "aws_internet_gateway", "main",
            vpc_id="aws_vpc.main.id",
            tags={"Name": f"{app_name}-igw"}
        )
        self.add_resource(igw)
        
        # Route Table
        route_table = TerraformResource(
            "aws_route_table", "public",
            vpc_id="aws_vpc.main.id",
            route=[
                {
                    "cidr_block": "0.0.0.0/0",
                    "gateway_id": "aws_internet_gateway.main.id"
                }
            ],
            tags={"Name": f"{app_name}-public-rt"}
        )
        self.add_resource(route_table)
        
        # Security Group
        security_group = TerraformResource(
            "aws_security_group", "web",
            name=f"{app_name}-web-sg",
            description=f"Security group for {app_name} web servers",
            vpc_id="aws_vpc.main.id",
            ingress=[
                {
                    "from_port": 80,
                    "to_port": 80,
                    "protocol": "tcp",
                    "cidr_blocks": ["0.0.0.0/0"]
                },
                {
                    "from_port": 443,
                    "to_port": 443,
                    "protocol": "tcp",
                    "cidr_blocks": ["0.0.0.0/0"]
                }
            ],
            egress=[
                {
                    "from_port": 0,
                    "to_port": 0,
                    "protocol": "-1",
                    "cidr_blocks": ["0.0.0.0/0"]
                }
            ],
            tags={"Name": f"{app_name}-web-sg"}
        )
        self.add_resource(security_group)
        
        # EC2 Instance
        instance = TerraformResource(
            "aws_instance", "web",
            ami="data.aws_ami.ubuntu.id",
            instance_type="t3.micro",
            subnet_id="aws_subnet.public.id",
            vpc_security_group_ids=["aws_security_group.web.id"],
            user_data="file('user-data.sh')",
            tags={"Name": f"{app_name}-web-server", "Environment": "var.environment"}
        )
        self.add_resource(instance)
        
        # Add outputs
        self.add_output("vpc_id", "aws_vpc.main.id", "VPC ID")
        self.add_output("instance_ip", "aws_instance.web.public_ip", "Web server public IP")
        self.add_output("instance_dns", "aws_instance.web.public_dns", "Web server public DNS")

# Comprehensive demonstration
print("Monitoring, CI/CD & Infrastructure örnekleri:")

async def devops_comprehensive_demo():
    # 1. Monitoring & Observability
    print("\n--- Monitoring & Observability ---")
    
    metrics = MetricsCollector()
    logger = StructuredLogger("web-app")
    
    # Setup log handlers
    def console_handler(log_entry: LogEntry):
        print(f"[{log_entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
              f"{log_entry.level.value} - {log_entry.message}")
    
    def json_handler(log_entry: LogEntry):
        # In production, this would write to file or send to log aggregator
        pass
    
    logger.add_handler(console_handler)
    logger.add_handler(json_handler)
    
    # Simulate application metrics and logs
    logger.info("Application starting", version="1.0.0", environment="production")
    
    for i in range(10):
        # Simulate HTTP requests
        metrics.counter("http_requests_total", labels={"method": "GET", "endpoint": "/api/users"})
        metrics.histogram("http_request_duration", 0.1 + i * 0.05, labels={"endpoint": "/api/users"})
        
        if i % 5 == 0:  # Simulate some errors
            metrics.counter("http_errors_total", labels={"method": "GET", "status": "500"})
            logger.error("Database connection failed", error_code="DB001")
    
    # Memory and CPU metrics
    metrics.gauge("memory_usage_percent", 75.5)
    metrics.gauge("cpu_usage_percent", 45.2)
    
    # Setup monitoring dashboard
    dashboard = MonitoringDashboard(metrics)
    
    # Create alerts
    dashboard.create_alert("High Error Rate", "http_errors_total", 5, "greater_than")
    dashboard.create_alert("High Memory Usage", "memory_usage_percent", 80, "greater_than")
    
    # Get dashboard data
    dashboard_data = dashboard.get_dashboard_data()
    print(f"\nSystem Health Score: {dashboard_data['system_health']['score']}/100")
    print(f"Status: {dashboard_data['system_health']['status']}")
    
    # 2. CI/CD Pipeline
    print(f"\n--- CI/CD Pipeline ---")
    
    # Setup repository
    repo = GitOpsRepository()
    
    # Create initial commit
    commit_id = repo.commit("Initial application setup", {
        "app.py": "# Main application file",
        "requirements.txt": "fastapi==0.104.1\nuvicorn==0.24.0",
        "Dockerfile": "FROM python:3.11\n...",
        "tests/test_app.py": "# Test files"
    })
    
    # Setup CI/CD pipeline
    pipeline = CICDPipeline(repo)
    
    # Set environment
    pipeline.set_environment({
        "PYTHON_VERSION": "3.11",
        "APP_NAME": "python-web-app",
        "ENVIRONMENT": "production"
    })
    
    # Add pipeline steps
    pipeline.add_step(PipelineStep(
        name="Code Quality Check",
        stage=PipelineStage.BUILD,
        script=[
            "echo 'Running code quality checks...'",
            "black --check .",
            "flake8 .",
            "mypy ."
        ]
    ))
    
    pipeline.add_step(PipelineStep(
        name="Unit Tests",
        stage=PipelineStage.TEST,
        script=[
            "echo 'Installing dependencies...'",
            "pip install -r requirements.txt",
            "pip install pytest pytest-cov",
            "pytest tests/ --cov=app --cov-report=xml"
        ]
    ))
    
    pipeline.add_step(PipelineStep(
        name="Security Scan",
        stage=PipelineStage.SECURITY,
        script=[
            "echo 'Running security scan...'",
            "pip install safety bandit",
            "safety check",
            "bandit -r app/"
        ]
    ))
    
    pipeline.add_step(PipelineStep(
        name="Build Docker Image",
        stage=PipelineStage.BUILD,
        script=[
            "echo 'Building Docker image...'",
            "docker build -t $APP_NAME:$BUILD_NUMBER .",
            "docker tag $APP_NAME:$BUILD_NUMBER $APP_NAME:latest"
        ],
        environment={"BUILD_NUMBER": "123"}
    ))
    
    pipeline.add_step(PipelineStep(
        name="Deploy to Production",
        stage=PipelineStage.DEPLOY,
        script=[
            "echo 'Deploying to production...'",
            "kubectl apply -f k8s/",
            "kubectl rollout status deployment/$APP_NAME-deployment"
        ]
    ))
    
    pipeline.add_step(PipelineStep(
        name="Health Check",
        stage=PipelineStage.VERIFY,
        script=[
            "echo 'Running health checks...'",
            "curl -f http://production-url/health",
            "echo 'Deployment verification complete'"
        ]
    ))
    
    # Run pipeline
    pipeline_result = await pipeline.run_pipeline(commit_id)
    
    # 3. Infrastructure as Code
    print(f"\n--- Infrastructure as Code ---")
    
    # Create infrastructure template
    infra = InfrastructureTemplate()
    infra.create_web_application_infrastructure("python-web-app")
    
    terraform_config = infra.generate_terraform()
    
    print("Generated Terraform configuration:")
    print("-" * 40)
    print(terraform_config[:1000] + "..." if len(terraform_config) > 1000 else terraform_config)
    
    # Create user data script for EC2
    user_data_script = """#!/bin/bash
apt-get update
apt-get install -y docker.io
systemctl start docker
systemctl enable docker

# Pull and run the application
docker pull python-web-app:latest
docker run -d -p 80:8000 python-web-app:latest
"""
    
    print(f"\nUser data script for EC2 instance:")
    print("-" * 40)
    print(user_data_script)
    
    print(f"\n🎉 DevOps pipeline demonstration completed!")

# Run comprehensive DevOps demo
asyncio.run(devops_comprehensive_demo())

print("\n" + "="*60)
print("DEPLOYMENT & DEVOPS TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Containerization & Docker")
print("2. Dockerfile & Docker Compose Generation")
print("3. Kubernetes Orchestration & Manifests")
print("4. Monitoring & Observability (Metrics, Logs, Alerts)")
print("5. CI/CD Pipeline Implementation")
print("6. GitOps & Repository Management")
print("7. Infrastructure as Code (Terraform)")
print("8. Automated Deployment & Health Checks")
print("9. Security Integration & Quality Gates")
print("10. Production-Ready DevOps Practices")

print("\n🎯 Tüm 17. Bölüm (Projeler) dosyaları tamamlandı!")