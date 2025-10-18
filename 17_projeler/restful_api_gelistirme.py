"""
Python RESTful API Geliştirme - Comprehensive Guide
FastAPI, Authentication, Database Integration, API Documentation

Bu dosyada modern RESTful API geliştirme teknikleri, FastAPI framework,
authentication/authorization, database operations ve API documentation incelenecek.
"""

import asyncio
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from enum import Enum
import json
import uuid
from contextlib import asynccontextmanager
import time

# Simulated external dependencies (in real project these would be actual imports)
class FastAPIRequest:
    """Simulated FastAPI Request"""
    def __init__(self, headers=None, query_params=None, path_params=None):
        self.headers = headers or {}
        self.query_params = query_params or {}
        self.path_params = path_params or {}

class HTTPException(Exception):
    """Simulated FastAPI HTTPException"""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)

# =============================================================================
# 1. FASTAPI APPLICATION STRUCTURE
# =============================================================================

print("=== FastAPI Application Structure ===")

class APIResponse:
    """Standardized API response structure"""
    
    def __init__(self, success: bool = True, data: Any = None, 
                 message: str = "", errors: List[str] = None, 
                 pagination: Dict = None):
        self.success = success
        self.data = data
        self.message = message
        self.errors = errors or []
        self.pagination = pagination
        self.timestamp = datetime.utcnow().isoformat()
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        result = {
            "success": self.success,
            "message": self.message,
            "timestamp": self.timestamp
        }
        
        if self.data is not None:
            result["data"] = self.data
        
        if self.errors:
            result["errors"] = self.errors
        
        if self.pagination:
            result["pagination"] = self.pagination
        
        return result

class HTTPStatus(Enum):
    """HTTP Status codes"""
    OK = 200
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500

class BaseModel:
    """Base Pydantic-like model"""
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dict(self):
        return {key: value for key, value in self.__dict__.items() 
                if not key.startswith('_')}

# Request/Response Models
class UserCreate(BaseModel):
    """User creation request model"""
    
    def __init__(self, email: str, password: str, first_name: str, 
                 last_name: str, phone: Optional[str] = None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        
        # Validation
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")

class UserResponse(BaseModel):
    """User response model"""
    
    def __init__(self, id: int, email: str, first_name: str, 
                 last_name: str, phone: Optional[str] = None, 
                 is_active: bool = True, created_at: datetime = None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()

class UserUpdate(BaseModel):
    """User update request model"""
    
    def __init__(self, first_name: Optional[str] = None, 
                 last_name: Optional[str] = None, 
                 phone: Optional[str] = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

class ProductCreate(BaseModel):
    """Product creation request model"""
    
    def __init__(self, name: str, description: str, price: float, 
                 category_id: int, stock_quantity: int = 0):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.stock_quantity = stock_quantity
        
        # Validation
        if not name:
            raise ValueError("Product name is required")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")

class ProductResponse(BaseModel):
    """Product response model"""
    
    def __init__(self, id: int, name: str, description: str, 
                 price: float, category_id: int, stock_quantity: int,
                 is_active: bool = True, created_at: datetime = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.stock_quantity = stock_quantity
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()

# FastAPI Application Structure Example
class FastAPIApp:
    """Simulated FastAPI application"""
    
    def __init__(self):
        self.routes = {}
        self.middleware = []
        self.startup_events = []
        self.shutdown_events = []
    
    def add_route(self, method: str, path: str, handler: callable):
        """Add route handler"""
        key = f"{method.upper()} {path}"
        self.routes[key] = handler
        print(f"📍 Route registered: {key}")
    
    def add_middleware(self, middleware: callable):
        """Add middleware"""
        self.middleware.append(middleware)
        print(f"🔧 Middleware registered: {middleware.__name__}")
    
    def on_startup(self, func: callable):
        """Add startup event"""
        self.startup_events.append(func)
        return func
    
    def on_shutdown(self, func: callable):
        """Add shutdown event"""
        self.shutdown_events.append(func)
        return func
    
    async def startup(self):
        """Execute startup events"""
        for event in self.startup_events:
            await event()
    
    async def shutdown(self):
        """Execute shutdown events"""
        for event in self.shutdown_events:
            await event()

# Application setup demonstration
print("FastAPI application structure örnekleri:")

app = FastAPIApp()

# Startup/shutdown events
@app.on_startup
async def startup_event():
    print("🚀 Application starting up...")
    # Initialize database connections, caches, etc.

@app.on_shutdown
async def shutdown_event():
    print("🛑 Application shutting down...")
    # Cleanup resources

# =============================================================================
# 2. AUTHENTICATION & AUTHORIZATION
# =============================================================================

print("\n=== Authentication & Authorization ===")

class TokenType(Enum):
    ACCESS = "access"
    REFRESH = "refresh"

@dataclass
class TokenData:
    """JWT token data"""
    user_id: int
    email: str
    token_type: TokenType
    exp: datetime
    iat: datetime

class PasswordManager:
    """Password hashing and verification"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using SHA-256 (in production, use bcrypt)"""
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{salt}${hashed}"
    
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """Verify password against hash"""
        try:
            salt, stored_hash = hashed_password.split('$')
            computed_hash = hashlib.sha256((password + salt).encode()).hexdigest()
            return computed_hash == stored_hash
        except:
            return False

class JWTManager:
    """JWT token management (simplified implementation)"""
    
    def __init__(self, secret_key: str, access_token_expire_minutes: int = 30):
        self.secret_key = secret_key
        self.access_token_expire_minutes = access_token_expire_minutes
    
    def create_access_token(self, user_id: int, email: str) -> str:
        """Create access token"""
        now = datetime.utcnow()
        exp = now + timedelta(minutes=self.access_token_expire_minutes)
        
        token_data = {
            "user_id": user_id,
            "email": email,
            "token_type": "access",
            "exp": exp.timestamp(),
            "iat": now.timestamp()
        }
        
        # Simplified JWT creation (in production, use proper JWT library)
        token_json = json.dumps(token_data)
        signature = hashlib.sha256((token_json + self.secret_key).encode()).hexdigest()
        return f"{secrets.token_urlsafe(32)}.{signature[:32]}"
    
    def create_refresh_token(self, user_id: int) -> str:
        """Create refresh token"""
        return secrets.token_urlsafe(64)
    
    def verify_token(self, token: str) -> Optional[TokenData]:
        """Verify and decode token (simplified)"""
        try:
            # In production, use proper JWT verification
            # This is a simplified example
            parts = token.split('.')
            if len(parts) != 2:
                return None
            
            # For demo, we'll create mock token data
            return TokenData(
                user_id=1,
                email="user@example.com",
                token_type=TokenType.ACCESS,
                exp=datetime.utcnow() + timedelta(hours=1),
                iat=datetime.utcnow()
            )
        except:
            return None

class AuthService:
    """Authentication service"""
    
    def __init__(self):
        self.jwt_manager = JWTManager("secret_key_change_in_production")
        self.password_manager = PasswordManager()
        # Mock user storage
        self.users = {}
        self.refresh_tokens = {}
    
    async def register_user(self, user_data: UserCreate) -> UserResponse:
        """Register new user"""
        # Check if user exists
        if any(user.email == user_data.email for user in self.users.values()):
            raise HTTPException(409, "User with this email already exists")
        
        # Create user
        user_id = len(self.users) + 1
        hashed_password = self.password_manager.hash_password(user_data.password)
        
        user = UserResponse(
            id=user_id,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone
        )
        
        # Store user (with hashed password)
        self.users[user_id] = {
            **user.dict(),
            "password_hash": hashed_password
        }
        
        print(f"👤 User registered: {user_data.email}")
        return user
    
    async def login(self, email: str, password: str) -> Dict[str, str]:
        """Authenticate user and return tokens"""
        # Find user
        user_data = None
        for user in self.users.values():
            if user["email"] == email:
                user_data = user
                break
        
        if not user_data:
            raise HTTPException(401, "Invalid credentials")
        
        # Verify password
        if not self.password_manager.verify_password(password, user_data["password_hash"]):
            raise HTTPException(401, "Invalid credentials")
        
        # Generate tokens
        access_token = self.jwt_manager.create_access_token(
            user_data["id"], user_data["email"]
        )
        refresh_token = self.jwt_manager.create_refresh_token(user_data["id"])
        
        # Store refresh token
        self.refresh_tokens[refresh_token] = {
            "user_id": user_data["id"],
            "created_at": datetime.utcnow()
        }
        
        print(f"🔑 User logged in: {email}")
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    async def get_current_user(self, token: str) -> Optional[UserResponse]:
        """Get current user from token"""
        token_data = self.jwt_manager.verify_token(token)
        if not token_data:
            return None
        
        user_data = self.users.get(token_data.user_id)
        if not user_data:
            return None
        
        return UserResponse(**{k: v for k, v in user_data.items() 
                             if k != "password_hash"})

# Role-Based Access Control
class Permission(Enum):
    READ_USERS = "read:users"
    WRITE_USERS = "write:users"
    DELETE_USERS = "delete:users"
    READ_PRODUCTS = "read:products"
    WRITE_PRODUCTS = "write:products"
    DELETE_PRODUCTS = "delete:products"
    ADMIN = "admin"

class Role(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
    GUEST = "guest"

class RBACService:
    """Role-Based Access Control Service"""
    
    def __init__(self):
        self.role_permissions = {
            Role.ADMIN: list(Permission),
            Role.MANAGER: [
                Permission.READ_USERS, Permission.WRITE_USERS,
                Permission.READ_PRODUCTS, Permission.WRITE_PRODUCTS
            ],
            Role.USER: [Permission.READ_PRODUCTS],
            Role.GUEST: []
        }
        self.user_roles = {}
    
    def assign_role(self, user_id: int, role: Role):
        """Assign role to user"""
        self.user_roles[user_id] = role
        print(f"👥 Role assigned: User {user_id} -> {role.value}")
    
    def check_permission(self, user_id: int, permission: Permission) -> bool:
        """Check if user has permission"""
        user_role = self.user_roles.get(user_id)
        if not user_role:
            return False
        
        allowed_permissions = self.role_permissions.get(user_role, [])
        return permission in allowed_permissions
    
    def require_permission(self, permission: Permission):
        """Decorator to require permission"""
        def decorator(func):
            async def wrapper(*args, **kwargs):
                # In real implementation, extract user from request context
                current_user_id = 1  # Mock current user
                
                if not self.check_permission(current_user_id, permission):
                    raise HTTPException(403, f"Permission required: {permission.value}")
                
                return await func(*args, **kwargs)
            return wrapper
        return decorator

# Authentication demonstration
print("Authentication & authorization örnekleri:")

auth_service = AuthService()
rbac_service = RBACService()

async def auth_demo():
    # Register user
    user_create = UserCreate(
        email="alice@example.com",
        password="securepassword123",
        first_name="Alice",
        last_name="Johnson",
        phone="+1234567890"
    )
    
    user = await auth_service.register_user(user_create)
    print(f"Registered user: {user.email}")
    
    # Assign role
    rbac_service.assign_role(user.id, Role.MANAGER)
    
    # Login
    tokens = await auth_service.login("alice@example.com", "securepassword123")
    print(f"Login successful: {tokens['token_type']} token received")
    
    # Get current user
    current_user = await auth_service.get_current_user(tokens["access_token"])
    print(f"Current user: {current_user.first_name} {current_user.last_name}")
    
    # Check permissions
    can_read_users = rbac_service.check_permission(user.id, Permission.READ_USERS)
    can_delete_users = rbac_service.check_permission(user.id, Permission.DELETE_USERS)
    
    print(f"Can read users: {can_read_users}")
    print(f"Can delete users: {can_delete_users}")

# Run authentication demo
asyncio.run(auth_demo())

# =============================================================================
# 3. DATABASE INTEGRATION
# =============================================================================

print("\n=== Database Integration ===")

class DatabaseConnection:
    """Simulated database connection"""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connected = False
        print(f"🔗 Database connection created: {connection_string}")
    
    async def connect(self):
        """Connect to database"""
        await asyncio.sleep(0.1)  # Simulate connection time
        self.connected = True
        print("✅ Database connected")
    
    async def disconnect(self):
        """Disconnect from database"""
        self.connected = False
        print("🔌 Database disconnected")
    
    async def execute(self, query: str, params: tuple = None) -> List[dict]:
        """Execute database query"""
        if not self.connected:
            raise Exception("Database not connected")
        
        # Simulate query execution
        await asyncio.sleep(0.01)
        print(f"📝 Executing query: {query}")
        
        # Mock results based on query type
        if "SELECT" in query.upper():
            if "users" in query.lower():
                return [{"id": 1, "email": "alice@example.com", "first_name": "Alice"}]
            elif "products" in query.lower():
                return [{"id": 1, "name": "Product A", "price": 29.99}]
        
        return []
    
    async def execute_many(self, query: str, params_list: List[tuple]) -> int:
        """Execute query with multiple parameter sets"""
        if not self.connected:
            raise Exception("Database not connected")
        
        await asyncio.sleep(0.05)  # Simulate execution time
        print(f"📝 Executing batch query: {query} ({len(params_list)} rows)")
        return len(params_list)

class BaseRepository:
    """Base repository pattern"""
    
    def __init__(self, db_connection: DatabaseConnection):
        self.db = db_connection
    
    async def get_by_id(self, table: str, id: int) -> Optional[dict]:
        """Get record by ID"""
        query = f"SELECT * FROM {table} WHERE id = ?"
        results = await self.db.execute(query, (id,))
        return results[0] if results else None
    
    async def get_all(self, table: str, limit: int = 100, offset: int = 0) -> List[dict]:
        """Get all records with pagination"""
        query = f"SELECT * FROM {table} LIMIT ? OFFSET ?"
        return await self.db.execute(query, (limit, offset))
    
    async def create(self, table: str, data: dict) -> int:
        """Create new record"""
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        
        await self.db.execute(query, tuple(data.values()))
        # Return mock ID
        return len(data)  # Simplified
    
    async def update(self, table: str, id: int, data: dict) -> bool:
        """Update record"""
        set_clause = ", ".join([f"{key} = ?" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        
        await self.db.execute(query, tuple(list(data.values()) + [id]))
        return True
    
    async def delete(self, table: str, id: int) -> bool:
        """Delete record"""
        query = f"DELETE FROM {table} WHERE id = ?"
        await self.db.execute(query, (id,))
        return True

class UserRepository(BaseRepository):
    """User repository"""
    
    async def get_by_email(self, email: str) -> Optional[dict]:
        """Get user by email"""
        query = "SELECT * FROM users WHERE email = ?"
        results = await self.db.execute(query, (email,))
        return results[0] if results else None
    
    async def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create new user"""
        data = {
            "email": user_data.email,
            "password_hash": PasswordManager.hash_password(user_data.password),
            "first_name": user_data.first_name,
            "last_name": user_data.last_name,
            "phone": user_data.phone,
            "is_active": True,
            "created_at": datetime.utcnow()
        }
        
        user_id = await self.create("users", data)
        
        return UserResponse(
            id=user_id,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            phone=user_data.phone
        )
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> bool:
        """Update user"""
        # Only update non-None fields
        update_data = {}
        if user_data.first_name is not None:
            update_data["first_name"] = user_data.first_name
        if user_data.last_name is not None:
            update_data["last_name"] = user_data.last_name
        if user_data.phone is not None:
            update_data["phone"] = user_data.phone
        
        if update_data:
            update_data["updated_at"] = datetime.utcnow()
            return await self.update("users", user_id, update_data)
        
        return True

class ProductRepository(BaseRepository):
    """Product repository"""
    
    async def get_by_category(self, category_id: int) -> List[dict]:
        """Get products by category"""
        query = "SELECT * FROM products WHERE category_id = ? AND is_active = true"
        return await self.db.execute(query, (category_id,))
    
    async def search_products(self, search_term: str) -> List[dict]:
        """Search products by name or description"""
        query = """
        SELECT * FROM products 
        WHERE (name LIKE ? OR description LIKE ?) AND is_active = true
        """
        pattern = f"%{search_term}%"
        return await self.db.execute(query, (pattern, pattern))
    
    async def create_product(self, product_data: ProductCreate) -> ProductResponse:
        """Create new product"""
        data = {
            "name": product_data.name,
            "description": product_data.description,
            "price": product_data.price,
            "category_id": product_data.category_id,
            "stock_quantity": product_data.stock_quantity,
            "is_active": True,
            "created_at": datetime.utcnow()
        }
        
        product_id = await self.create("products", data)
        
        return ProductResponse(
            id=product_id,
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            category_id=product_data.category_id,
            stock_quantity=product_data.stock_quantity
        )
    
    async def update_stock(self, product_id: int, quantity_change: int) -> bool:
        """Update product stock"""
        # In real implementation, this would be atomic
        product = await self.get_by_id("products", product_id)
        if not product:
            return False
        
        new_quantity = product.get("stock_quantity", 0) + quantity_change
        if new_quantity < 0:
            raise ValueError("Insufficient stock")
        
        return await self.update("products", product_id, {
            "stock_quantity": new_quantity,
            "updated_at": datetime.utcnow()
        })

# Database service layer
class UserService:
    """User service layer"""
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    async def create_user(self, user_data: UserCreate) -> UserResponse:
        """Create new user with business logic"""
        # Check if user already exists
        existing_user = await self.user_repository.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(409, "User with this email already exists")
        
        return await self.user_repository.create_user(user_data)
    
    async def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID"""
        user_data = await self.user_repository.get_by_id("users", user_id)
        if not user_data:
            return None
        
        return UserResponse(**{k: v for k, v in user_data.items() 
                             if k != "password_hash"})
    
    async def update_user_profile(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        """Update user profile"""
        # Check if user exists
        existing_user = await self.user_repository.get_by_id("users", user_id)
        if not existing_user:
            raise HTTPException(404, "User not found")
        
        # Update user
        success = await self.user_repository.update_user(user_id, user_data)
        if not success:
            raise HTTPException(500, "Failed to update user")
        
        # Return updated user
        return await self.get_user_by_id(user_id)

# Database integration demonstration
print("Database integration örnekleri:")

async def database_demo():
    # Setup database connection
    db = DatabaseConnection("postgresql://localhost/ecommerce")
    await db.connect()
    
    # Setup repositories
    user_repo = UserRepository(db)
    product_repo = ProductRepository(db)
    
    # Setup services
    user_service = UserService(user_repo)
    
    try:
        # Create user
        user_create = UserCreate(
            email="bob@example.com",
            password="password123",
            first_name="Bob",
            last_name="Smith"
        )
        
        user = await user_service.create_user(user_create)
        print(f"Created user: {user.email}")
        
        # Update user
        user_update = UserUpdate(phone="+1987654321")
        updated_user = await user_service.update_user_profile(user.id, user_update)
        print(f"Updated user phone: {updated_user.phone}")
        
        # Create product
        product_create = ProductCreate(
            name="Laptop",
            description="Gaming laptop with RTX 4080",
            price=1599.99,
            category_id=1,
            stock_quantity=10
        )
        
        product = await product_repo.create_product(product_create)
        print(f"Created product: {product.name}")
        
        # Update stock
        await product_repo.update_stock(product.id, -2)  # Sell 2 units
        print("Stock updated successfully")
        
    finally:
        await db.disconnect()

# Run database demo
asyncio.run(database_demo())

# =============================================================================
# 4. API ENDPOINTS IMPLEMENTATION
# =============================================================================

print("\n=== API Endpoints Implementation ===")

class PaginationParams:
    """Pagination parameters"""
    
    def __init__(self, page: int = 1, limit: int = 20):
        self.page = max(1, page)
        self.limit = max(1, min(100, limit))  # Max 100 items per page
        self.offset = (self.page - 1) * self.limit

class APIController:
    """Base API controller"""
    
    def __init__(self):
        self.request_count = 0
    
    async def handle_request(self, handler: callable, *args, **kwargs):
        """Handle API request with error handling and logging"""
        self.request_count += 1
        start_time = time.time()
        
        try:
            print(f"🔄 Processing request #{self.request_count}")
            result = await handler(*args, **kwargs)
            
            duration = time.time() - start_time
            print(f"✅ Request completed in {duration:.3f}s")
            
            return APIResponse(success=True, data=result)
        
        except HTTPException as e:
            duration = time.time() - start_time
            print(f"❌ HTTP error in {duration:.3f}s: {e.status_code} - {e.detail}")
            
            return APIResponse(
                success=False,
                message=e.detail,
                errors=[e.detail]
            )
        
        except Exception as e:
            duration = time.time() - start_time
            print(f"💥 Unexpected error in {duration:.3f}s: {str(e)}")
            
            return APIResponse(
                success=False,
                message="Internal server error",
                errors=["An unexpected error occurred"]
            )

class UserController(APIController):
    """User management API controller"""
    
    def __init__(self, user_service: UserService, auth_service: AuthService):
        super().__init__()
        self.user_service = user_service
        self.auth_service = auth_service
    
    async def register(self, user_data: UserCreate) -> APIResponse:
        """POST /api/v1/users/register"""
        
        async def handler():
            user = await self.auth_service.register_user(user_data)
            return user.dict()
        
        return await self.handle_request(handler)
    
    async def login(self, email: str, password: str) -> APIResponse:
        """POST /api/v1/users/login"""
        
        async def handler():
            tokens = await self.auth_service.login(email, password)
            return tokens
        
        return await self.handle_request(handler)
    
    async def get_profile(self, current_user: UserResponse) -> APIResponse:
        """GET /api/v1/users/me"""
        
        async def handler():
            return current_user.dict()
        
        return await self.handle_request(handler)
    
    async def update_profile(self, user_id: int, user_data: UserUpdate) -> APIResponse:
        """PUT /api/v1/users/me"""
        
        async def handler():
            updated_user = await self.user_service.update_user_profile(user_id, user_data)
            return updated_user.dict()
        
        return await self.handle_request(handler)
    
    async def get_user(self, user_id: int) -> APIResponse:
        """GET /api/v1/users/{user_id}"""
        
        async def handler():
            user = await self.user_service.get_user_by_id(user_id)
            if not user:
                raise HTTPException(404, "User not found")
            return user.dict()
        
        return await self.handle_request(handler)

class ProductController(APIController):
    """Product management API controller"""
    
    def __init__(self, product_repository: ProductRepository):
        super().__init__()
        self.product_repository = product_repository
    
    async def create_product(self, product_data: ProductCreate) -> APIResponse:
        """POST /api/v1/products"""
        
        async def handler():
            product = await self.product_repository.create_product(product_data)
            return product.dict()
        
        return await self.handle_request(handler)
    
    async def get_product(self, product_id: int) -> APIResponse:
        """GET /api/v1/products/{product_id}"""
        
        async def handler():
            product = await self.product_repository.get_by_id("products", product_id)
            if not product:
                raise HTTPException(404, "Product not found")
            return product
        
        return await self.handle_request(handler)
    
    async def list_products(self, pagination: PaginationParams, 
                           category_id: Optional[int] = None,
                           search: Optional[str] = None) -> APIResponse:
        """GET /api/v1/products"""
        
        async def handler():
            if search:
                products = await self.product_repository.search_products(search)
            elif category_id:
                products = await self.product_repository.get_by_category(category_id)
            else:
                products = await self.product_repository.get_all(
                    "products", pagination.limit, pagination.offset
                )
            
            # Calculate pagination info
            total_count = len(products)  # Simplified
            total_pages = (total_count + pagination.limit - 1) // pagination.limit
            
            pagination_info = {
                "page": pagination.page,
                "limit": pagination.limit,
                "total": total_count,
                "pages": total_pages,
                "has_next": pagination.page < total_pages,
                "has_prev": pagination.page > 1
            }
            
            return {
                "products": products,
                "pagination": pagination_info
            }
        
        result = await self.handle_request(handler)
        
        # Move pagination to response level
        if result.success and result.data and "pagination" in result.data:
            result.pagination = result.data.pop("pagination")
            result.data = result.data["products"]
        
        return result
    
    async def update_stock(self, product_id: int, quantity_change: int) -> APIResponse:
        """PATCH /api/v1/products/{product_id}/stock"""
        
        async def handler():
            success = await self.product_repository.update_stock(
                product_id, quantity_change
            )
            if not success:
                raise HTTPException(404, "Product not found")
            
            updated_product = await self.product_repository.get_by_id(
                "products", product_id
            )
            return updated_product
        
        return await self.handle_request(handler)

# API Router simulation
class APIRouter:
    """Simulated FastAPI router"""
    
    def __init__(self, prefix: str = ""):
        self.prefix = prefix
        self.routes = []
    
    def add_route(self, method: str, path: str, handler: callable, 
                  tags: List[str] = None, summary: str = ""):
        """Add route to router"""
        full_path = f"{self.prefix}{path}"
        route = {
            "method": method,
            "path": full_path,
            "handler": handler,
            "tags": tags or [],
            "summary": summary
        }
        self.routes.append(route)
        print(f"📍 API Route: {method} {full_path}")

# API endpoints demonstration
print("API endpoints implementation örnekleri:")

async def api_demo():
    # Setup dependencies
    db = DatabaseConnection("postgresql://localhost/ecommerce")
    await db.connect()
    
    user_repo = UserRepository(db)
    product_repo = ProductRepository(db)
    user_service = UserService(user_repo)
    auth_service = AuthService()
    
    # Setup controllers
    user_controller = UserController(user_service, auth_service)
    product_controller = ProductController(product_repo)
    
    # Setup routers
    user_router = APIRouter(prefix="/api/v1/users")
    product_router = APIRouter(prefix="/api/v1/products")
    
    # Register user routes
    user_router.add_route("POST", "/register", user_controller.register,
                         tags=["Authentication"], summary="Register new user")
    user_router.add_route("POST", "/login", user_controller.login,
                         tags=["Authentication"], summary="User login")
    user_router.add_route("GET", "/me", user_controller.get_profile,
                         tags=["Users"], summary="Get current user profile")
    
    # Register product routes
    product_router.add_route("POST", "", product_controller.create_product,
                           tags=["Products"], summary="Create new product")
    product_router.add_route("GET", "", product_controller.list_products,
                           tags=["Products"], summary="List products")
    product_router.add_route("GET", "/{product_id}", product_controller.get_product,
                           tags=["Products"], summary="Get product by ID")
    
    try:
        # Simulate API requests
        print("\n--- User Registration ---")
        user_create = UserCreate(
            email="charlie@example.com",
            password="securepass123",
            first_name="Charlie",
            last_name="Brown"
        )
        
        register_response = await user_controller.register(user_create)
        print(f"Registration response: {register_response.to_dict()}")
        
        print("\n--- User Login ---")
        login_response = await user_controller.login("charlie@example.com", "securepass123")
        print(f"Login response: {login_response.to_dict()}")
        
        print("\n--- Product Creation ---")
        product_create = ProductCreate(
            name="Smartphone",
            description="Latest flagship smartphone",
            price=899.99,
            category_id=2,
            stock_quantity=50
        )
        
        product_response = await product_controller.create_product(product_create)
        print(f"Product creation response: {product_response.to_dict()}")
        
        print("\n--- Product Listing ---")
        pagination = PaginationParams(page=1, limit=10)
        list_response = await product_controller.list_products(pagination)
        print(f"Product list response: {list_response.to_dict()}")
        
        print("\n--- Stock Update ---")
        stock_response = await product_controller.update_stock(1, -5)
        print(f"Stock update response: {stock_response.to_dict()}")
        
    finally:
        await db.disconnect()

# Run API demo
asyncio.run(api_demo())

print("\n" + "="*60)
print("RESTFUL API GELİŞTİRME TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. FastAPI Application Structure")
print("2. Authentication & Authorization (JWT, RBAC)")
print("3. Database Integration (Repository Pattern)")
print("4. API Endpoints Implementation")
print("5. Request/Response Models")
print("6. Error Handling & Logging")
print("7. Pagination & Search")

print("\nBir sonraki dosya: mikroservis_mimarisi.py")