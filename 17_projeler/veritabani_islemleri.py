"""
Python Veritabanı İşlemleri - Comprehensive Guide
ORM, Connection Pooling, Migrations, Transactions, Performance Optimization

Bu dosyada modern veritabanı işlemleri, ORM kullanımı, connection pooling,
migration yönetimi, transaction handling ve performans optimizasyonu incelenecek.
"""

import asyncio
import sqlite3
import hashlib
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union, Tuple, Callable, Set
from dataclasses import dataclass, field
from enum import Enum
import uuid
from contextlib import asynccontextmanager
import threading
from collections import defaultdict
import re

# =============================================================================
# 1. DATABASE ABSTRACTION LAYER
# =============================================================================

print("=== Database Abstraction Layer ===")

class DatabaseType(Enum):
    """Supported database types"""
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"
    MYSQL = "mysql"
    MONGODB = "mongodb"

class ColumnType(Enum):
    """Database column types"""
    INTEGER = "INTEGER"
    STRING = "VARCHAR"
    TEXT = "TEXT"
    BOOLEAN = "BOOLEAN"
    FLOAT = "REAL"
    DATETIME = "TIMESTAMP"
    JSON = "JSON"

@dataclass
class Column:
    """Database column definition"""
    name: str
    type: ColumnType
    nullable: bool = True
    primary_key: bool = False
    unique: bool = False
    default: Any = None
    length: Optional[int] = None
    foreign_key: Optional[str] = None
    
    def to_sql(self, db_type: DatabaseType) -> str:
        """Convert to SQL column definition"""
        sql_parts = [self.name]
        
        # Type mapping
        if db_type == DatabaseType.SQLITE:
            type_map = {
                ColumnType.INTEGER: "INTEGER",
                ColumnType.STRING: f"VARCHAR({self.length or 255})",
                ColumnType.TEXT: "TEXT",
                ColumnType.BOOLEAN: "BOOLEAN",
                ColumnType.FLOAT: "REAL",
                ColumnType.DATETIME: "TIMESTAMP",
                ColumnType.JSON: "TEXT"
            }
        else:  # PostgreSQL/MySQL
            type_map = {
                ColumnType.INTEGER: "INTEGER",
                ColumnType.STRING: f"VARCHAR({self.length or 255})",
                ColumnType.TEXT: "TEXT",
                ColumnType.BOOLEAN: "BOOLEAN",
                ColumnType.FLOAT: "REAL",
                ColumnType.DATETIME: "TIMESTAMP",
                ColumnType.JSON: "JSONB" if db_type == DatabaseType.POSTGRESQL else "JSON"
            }
        
        sql_parts.append(type_map.get(self.type, "TEXT"))
        
        # Constraints
        if self.primary_key:
            sql_parts.append("PRIMARY KEY")
        
        if not self.nullable:
            sql_parts.append("NOT NULL")
        
        if self.unique and not self.primary_key:
            sql_parts.append("UNIQUE")
        
        if self.default is not None:
            if isinstance(self.default, str):
                sql_parts.append(f"DEFAULT '{self.default}'")
            else:
                sql_parts.append(f"DEFAULT {self.default}")
        
        return " ".join(sql_parts)

@dataclass
class Table:
    """Database table definition"""
    name: str
    columns: List[Column] = field(default_factory=list)
    indexes: List[str] = field(default_factory=list)
    
    def add_column(self, column: Column):
        """Add column to table"""
        self.columns.append(column)
    
    def get_primary_key(self) -> Optional[Column]:
        """Get primary key column"""
        for column in self.columns:
            if column.primary_key:
                return column
        return None
    
    def to_create_sql(self, db_type: DatabaseType) -> str:
        """Generate CREATE TABLE SQL"""
        if not self.columns:
            raise ValueError("Table must have at least one column")
        
        column_definitions = []
        for column in self.columns:
            column_definitions.append(column.to_sql(db_type))
        
        # Foreign key constraints
        foreign_keys = []
        for column in self.columns:
            if column.foreign_key:
                foreign_keys.append(
                    f"FOREIGN KEY ({column.name}) REFERENCES {column.foreign_key}"
                )
        
        all_definitions = column_definitions + foreign_keys
        
        sql = f"CREATE TABLE {self.name} (\n"
        sql += ",\n".join(f"    {definition}" for definition in all_definitions)
        sql += "\n)"
        
        return sql

class DatabaseConnection:
    """Database connection wrapper"""
    
    def __init__(self, connection_string: str, db_type: DatabaseType):
        self.connection_string = connection_string
        self.db_type = db_type
        self.connection = None
        self.in_transaction = False
    
    async def connect(self):
        """Connect to database"""
        if self.db_type == DatabaseType.SQLITE:
            # For demo purposes, use SQLite
            self.connection = sqlite3.connect(":memory:")
            self.connection.row_factory = sqlite3.Row
        else:
            # In production, use appropriate database drivers
            print(f"Connecting to {self.db_type.value} database...")
            # Simulated connection
            self.connection = "simulated_connection"
        
        print(f"✅ Connected to {self.db_type.value} database")
    
    async def disconnect(self):
        """Disconnect from database"""
        if self.connection and self.db_type == DatabaseType.SQLITE:
            self.connection.close()
        self.connection = None
        print(f"🔌 Disconnected from {self.db_type.value} database")
    
    async def execute(self, query: str, params: tuple = None) -> Any:
        """Execute SQL query"""
        if not self.connection:
            raise RuntimeError("Not connected to database")
        
        print(f"📝 Executing: {query}")
        if params:
            print(f"   Parameters: {params}")
        
        if self.db_type == DatabaseType.SQLITE:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            
            if query.strip().upper().startswith('SELECT'):
                return [dict(row) for row in cursor.fetchall()]
            elif query.strip().upper().startswith('INSERT'):
                return cursor.lastrowid
            else:
                return cursor.rowcount
        else:
            # Simulated execution for other databases
            await asyncio.sleep(0.01)
            return []
    
    async def execute_many(self, query: str, params_list: List[tuple]) -> int:
        """Execute query with multiple parameter sets"""
        if not self.connection:
            raise RuntimeError("Not connected to database")
        
        print(f"📝 Executing batch: {query} ({len(params_list)} rows)")
        
        if self.db_type == DatabaseType.SQLITE:
            cursor = self.connection.cursor()
            cursor.executemany(query, params_list)
            return cursor.rowcount
        else:
            await asyncio.sleep(0.01 * len(params_list))
            return len(params_list)
    
    async def begin_transaction(self):
        """Begin transaction"""
        if self.db_type == DatabaseType.SQLITE:
            await self.execute("BEGIN TRANSACTION")
        else:
            await self.execute("BEGIN")
        
        self.in_transaction = True
        print("🔄 Transaction started")
    
    async def commit(self):
        """Commit transaction"""
        if self.db_type == DatabaseType.SQLITE:
            self.connection.commit()
        else:
            await self.execute("COMMIT")
        
        self.in_transaction = False
        print("✅ Transaction committed")
    
    async def rollback(self):
        """Rollback transaction"""
        if self.db_type == DatabaseType.SQLITE:
            self.connection.rollback()
        else:
            await self.execute("ROLLBACK")
        
        self.in_transaction = False
        print("🔙 Transaction rolled back")

class ConnectionPool:
    """Database connection pool"""
    
    def __init__(self, connection_string: str, db_type: DatabaseType, 
                 min_connections: int = 2, max_connections: int = 10):
        self.connection_string = connection_string
        self.db_type = db_type
        self.min_connections = min_connections
        self.max_connections = max_connections
        self.available_connections = []
        self.used_connections = set()
        self.lock = threading.Lock()
        self._initialized = False
    
    async def initialize(self):
        """Initialize connection pool"""
        if self._initialized:
            return
        
        for i in range(self.min_connections):
            conn = DatabaseConnection(self.connection_string, self.db_type)
            await conn.connect()
            self.available_connections.append(conn)
        
        self._initialized = True
        print(f"🏊 Connection pool initialized ({self.min_connections} connections)")
    
    async def get_connection(self) -> DatabaseConnection:
        """Get connection from pool"""
        with self.lock:
            if self.available_connections:
                conn = self.available_connections.pop()
                self.used_connections.add(conn)
                print(f"📤 Connection acquired from pool (available: {len(self.available_connections)})")
                return conn
            
            elif len(self.used_connections) < self.max_connections:
                conn = DatabaseConnection(self.connection_string, self.db_type)
                await conn.connect()
                self.used_connections.add(conn)
                print(f"🆕 New connection created (total: {len(self.used_connections)})")
                return conn
            
            else:
                raise RuntimeError("Connection pool exhausted")
    
    async def return_connection(self, connection: DatabaseConnection):
        """Return connection to pool"""
        with self.lock:
            if connection in self.used_connections:
                self.used_connections.remove(connection)
                
                if len(self.available_connections) < self.min_connections:
                    self.available_connections.append(connection)
                    print(f"📥 Connection returned to pool (available: {len(self.available_connections)})")
                else:
                    await connection.disconnect()
                    print("🗑️ Excess connection closed")
    
    @asynccontextmanager
    async def connection(self):
        """Context manager for connection handling"""
        conn = await self.get_connection()
        try:
            yield conn
        finally:
            await self.return_connection(conn)
    
    async def close_all(self):
        """Close all connections"""
        all_connections = list(self.available_connections) + list(self.used_connections)
        
        for conn in all_connections:
            await conn.disconnect()
        
        self.available_connections.clear()
        self.used_connections.clear()
        print("🚫 All connections closed")

# Database abstraction demonstration
print("Database abstraction layer örnekleri:")

async def database_abstraction_demo():
    # Define table schema
    users_table = Table("users")
    users_table.add_column(Column("id", ColumnType.INTEGER, primary_key=True, nullable=False))
    users_table.add_column(Column("email", ColumnType.STRING, length=255, unique=True, nullable=False))
    users_table.add_column(Column("password_hash", ColumnType.STRING, length=255, nullable=False))
    users_table.add_column(Column("first_name", ColumnType.STRING, length=100, nullable=False))
    users_table.add_column(Column("last_name", ColumnType.STRING, length=100, nullable=False))
    users_table.add_column(Column("is_active", ColumnType.BOOLEAN, default=True))
    users_table.add_column(Column("created_at", ColumnType.DATETIME, default="CURRENT_TIMESTAMP"))
    
    # Generate SQL
    create_sql = users_table.to_create_sql(DatabaseType.SQLITE)
    print("Generated SQL:")
    print(create_sql)
    
    # Setup connection pool
    pool = ConnectionPool("sqlite:///:memory:", DatabaseType.SQLITE)
    await pool.initialize()
    
    try:
        # Use connection from pool
        async with pool.connection() as conn:
            # Create table
            await conn.execute(create_sql)
            
            # Insert data
            await conn.execute(
                "INSERT INTO users (email, password_hash, first_name, last_name) VALUES (?, ?, ?, ?)",
                ("alice@example.com", "hashed_password", "Alice", "Johnson")
            )
            
            # Query data
            results = await conn.execute("SELECT * FROM users")
            print(f"Query results: {results}")
    
    finally:
        await pool.close_all()

# Run database abstraction demo
asyncio.run(database_abstraction_demo())

# =============================================================================
# 2. ORM IMPLEMENTATION
# =============================================================================

print("\n=== ORM Implementation ===")

class Model:
    """Base ORM model"""
    
    _table_name: str = ""
    _columns: Dict[str, Column] = {}
    _connection_pool: ConnectionPool = None
    
    def __init__(self, **kwargs):
        self._data = {}
        self._changed_fields = set()
        self._is_new = True
        
        # Set attributes from kwargs
        for key, value in kwargs.items():
            if key in self._columns:
                setattr(self, key, value)
    
    def __setattr__(self, name: str, value: Any):
        if name.startswith('_') or name not in self._columns:
            super().__setattr__(name, value)
        else:
            if hasattr(self, '_data') and name in self._data:
                if self._data[name] != value:
                    self._changed_fields.add(name)
            else:
                if not hasattr(self, '_changed_fields'):
                    self._changed_fields = set()
                self._changed_fields.add(name)
            
            if not hasattr(self, '_data'):
                self._data = {}
            self._data[name] = value
    
    def __getattr__(self, name: str):
        if name in self._data:
            return self._data[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    @classmethod
    def set_connection_pool(cls, pool: ConnectionPool):
        """Set connection pool for all models"""
        cls._connection_pool = pool
    
    @classmethod
    async def create_table(cls):
        """Create database table for model"""
        if not cls._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        table = Table(cls._table_name)
        for column in cls._columns.values():
            table.add_column(column)
        
        async with cls._connection_pool.connection() as conn:
            sql = table.to_create_sql(DatabaseType.SQLITE)
            await conn.execute(sql)
            print(f"📋 Table created: {cls._table_name}")
    
    async def save(self):
        """Save model instance"""
        if not self._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        async with self._connection_pool.connection() as conn:
            if self._is_new:
                # Insert new record
                columns = list(self._data.keys())
                placeholders = ", ".join(["?" for _ in columns])
                values = [self._data[col] for col in columns]
                
                sql = f"INSERT INTO {self._table_name} ({', '.join(columns)}) VALUES ({placeholders})"
                result = await conn.execute(sql, tuple(values))
                
                # Set primary key if auto-generated
                pk_column = self._get_primary_key_column()
                if pk_column and pk_column.name not in self._data:
                    setattr(self, pk_column.name, result)
                
                self._is_new = False
                print(f"✅ Created {self._table_name} record")
            
            elif self._changed_fields:
                # Update existing record
                pk_column = self._get_primary_key_column()
                if not pk_column or pk_column.name not in self._data:
                    raise RuntimeError("Cannot update record without primary key")
                
                set_clauses = []
                values = []
                
                for field in self._changed_fields:
                    set_clauses.append(f"{field} = ?")
                    values.append(self._data[field])
                
                values.append(self._data[pk_column.name])
                
                sql = f"UPDATE {self._table_name} SET {', '.join(set_clauses)} WHERE {pk_column.name} = ?"
                await conn.execute(sql, tuple(values))
                
                self._changed_fields.clear()
                print(f"✅ Updated {self._table_name} record")
    
    async def delete(self):
        """Delete model instance"""
        if not self._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        pk_column = self._get_primary_key_column()
        if not pk_column or pk_column.name not in self._data:
            raise RuntimeError("Cannot delete record without primary key")
        
        async with self._connection_pool.connection() as conn:
            sql = f"DELETE FROM {self._table_name} WHERE {pk_column.name} = ?"
            await conn.execute(sql, (self._data[pk_column.name],))
            print(f"🗑️ Deleted {self._table_name} record")
    
    @classmethod
    async def find_by_id(cls, id_value: Any):
        """Find record by primary key"""
        if not cls._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        pk_column = cls._get_primary_key_column()
        if not pk_column:
            raise RuntimeError("No primary key defined")
        
        async with cls._connection_pool.connection() as conn:
            sql = f"SELECT * FROM {cls._table_name} WHERE {pk_column.name} = ?"
            results = await conn.execute(sql, (id_value,))
            
            if results:
                instance = cls()
                instance._data = dict(results[0])
                instance._is_new = False
                instance._changed_fields.clear()
                return instance
        
        return None
    
    @classmethod
    async def find_all(cls, limit: int = None, offset: int = None):
        """Find all records"""
        if not cls._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        sql = f"SELECT * FROM {cls._table_name}"
        params = []
        
        if limit:
            sql += " LIMIT ?"
            params.append(limit)
            
            if offset:
                sql += " OFFSET ?"
                params.append(offset)
        
        async with cls._connection_pool.connection() as conn:
            results = await conn.execute(sql, tuple(params) if params else None)
            
            instances = []
            for row in results:
                instance = cls()
                instance._data = dict(row)
                instance._is_new = False
                instance._changed_fields.clear()
                instances.append(instance)
            
            return instances
    
    @classmethod
    async def find_where(cls, **conditions):
        """Find records with conditions"""
        if not cls._connection_pool:
            raise RuntimeError("Connection pool not set")
        
        where_clauses = []
        values = []
        
        for field, value in conditions.items():
            if field in cls._columns:
                where_clauses.append(f"{field} = ?")
                values.append(value)
        
        if not where_clauses:
            return await cls.find_all()
        
        sql = f"SELECT * FROM {cls._table_name} WHERE {' AND '.join(where_clauses)}"
        
        async with cls._connection_pool.connection() as conn:
            results = await conn.execute(sql, tuple(values))
            
            instances = []
            for row in results:
                instance = cls()
                instance._data = dict(row)
                instance._is_new = False
                instance._changed_fields.clear()
                instances.append(instance)
            
            return instances
    
    @classmethod
    def _get_primary_key_column(cls) -> Optional[Column]:
        """Get primary key column"""
        for column in cls._columns.values():
            if column.primary_key:
                return column
        return None
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return self._data.copy()

# Model implementations
class User(Model):
    """User model"""
    
    _table_name = "users"
    _columns = {
        "id": Column("id", ColumnType.INTEGER, primary_key=True, nullable=False),
        "email": Column("email", ColumnType.STRING, length=255, unique=True, nullable=False),
        "password_hash": Column("password_hash", ColumnType.STRING, length=255, nullable=False),
        "first_name": Column("first_name", ColumnType.STRING, length=100, nullable=False),
        "last_name": Column("last_name", ColumnType.STRING, length=100, nullable=False),
        "is_active": Column("is_active", ColumnType.BOOLEAN, default=True),
        "created_at": Column("created_at", ColumnType.DATETIME)
    }
    
    @property
    def full_name(self) -> str:
        """Get full name"""
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    async def find_by_email(cls, email: str):
        """Find user by email"""
        results = await cls.find_where(email=email)
        return results[0] if results else None

class Product(Model):
    """Product model"""
    
    _table_name = "products"
    _columns = {
        "id": Column("id", ColumnType.INTEGER, primary_key=True, nullable=False),
        "name": Column("name", ColumnType.STRING, length=255, nullable=False),
        "description": Column("description", ColumnType.TEXT),
        "price": Column("price", ColumnType.FLOAT, nullable=False),
        "stock_quantity": Column("stock_quantity", ColumnType.INTEGER, default=0),
        "category_id": Column("category_id", ColumnType.INTEGER, foreign_key="categories(id)"),
        "is_active": Column("is_active", ColumnType.BOOLEAN, default=True),
        "created_at": Column("created_at", ColumnType.DATETIME)
    }
    
    async def update_stock(self, quantity_change: int):
        """Update stock quantity"""
        self.stock_quantity = (self.stock_quantity or 0) + quantity_change
        if self.stock_quantity < 0:
            raise ValueError("Insufficient stock")
        await self.save()

class Order(Model):
    """Order model"""
    
    _table_name = "orders"
    _columns = {
        "id": Column("id", ColumnType.INTEGER, primary_key=True, nullable=False),
        "user_id": Column("user_id", ColumnType.INTEGER, foreign_key="users(id)", nullable=False),
        "total_amount": Column("total_amount", ColumnType.FLOAT, nullable=False),
        "status": Column("status", ColumnType.STRING, length=50, default="pending"),
        "created_at": Column("created_at", ColumnType.DATETIME),
        "updated_at": Column("updated_at", ColumnType.DATETIME)
    }

# Query builder
class QueryBuilder:
    """SQL query builder"""
    
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.select_fields = ["*"]
        self.where_conditions = []
        self.where_params = []
        self.join_clauses = []
        self.order_by_clauses = []
        self.group_by_clauses = []
        self.having_conditions = []
        self.limit_value = None
        self.offset_value = None
    
    def select(self, *fields):
        """Set SELECT fields"""
        self.select_fields = list(fields) if fields else ["*"]
        return self
    
    def where(self, condition: str, *params):
        """Add WHERE condition"""
        self.where_conditions.append(condition)
        self.where_params.extend(params)
        return self
    
    def join(self, table: str, on_condition: str, join_type: str = "INNER"):
        """Add JOIN clause"""
        self.join_clauses.append(f"{join_type} JOIN {table} ON {on_condition}")
        return self
    
    def order_by(self, field: str, direction: str = "ASC"):
        """Add ORDER BY clause"""
        self.order_by_clauses.append(f"{field} {direction}")
        return self
    
    def group_by(self, *fields):
        """Add GROUP BY clause"""
        self.group_by_clauses.extend(fields)
        return self
    
    def having(self, condition: str, *params):
        """Add HAVING condition"""
        self.having_conditions.append(condition)
        self.where_params.extend(params)
        return self
    
    def limit(self, count: int):
        """Add LIMIT clause"""
        self.limit_value = count
        return self
    
    def offset(self, count: int):
        """Add OFFSET clause"""
        self.offset_value = count
        return self
    
    def build(self) -> Tuple[str, tuple]:
        """Build SQL query"""
        # SELECT clause
        sql_parts = [f"SELECT {', '.join(self.select_fields)}"]
        
        # FROM clause
        sql_parts.append(f"FROM {self.table_name}")
        
        # JOIN clauses
        sql_parts.extend(self.join_clauses)
        
        # WHERE clause
        if self.where_conditions:
            sql_parts.append(f"WHERE {' AND '.join(self.where_conditions)}")
        
        # GROUP BY clause
        if self.group_by_clauses:
            sql_parts.append(f"GROUP BY {', '.join(self.group_by_clauses)}")
        
        # HAVING clause
        if self.having_conditions:
            sql_parts.append(f"HAVING {' AND '.join(self.having_conditions)}")
        
        # ORDER BY clause
        if self.order_by_clauses:
            sql_parts.append(f"ORDER BY {', '.join(self.order_by_clauses)}")
        
        # LIMIT clause
        if self.limit_value:
            sql_parts.append(f"LIMIT {self.limit_value}")
        
        # OFFSET clause
        if self.offset_value:
            sql_parts.append(f"OFFSET {self.offset_value}")
        
        return " ".join(sql_parts), tuple(self.where_params)

# ORM demonstration
print("ORM implementation örnekleri:")

async def orm_demo():
    # Setup connection pool
    pool = ConnectionPool("sqlite:///:memory:", DatabaseType.SQLITE)
    await pool.initialize()
    
    # Set connection pool for models
    Model.set_connection_pool(pool)
    
    try:
        # Create tables
        await User.create_table()
        await Product.create_table()
        await Order.create_table()
        
        # Create users
        user1 = User(
            email="alice@example.com",
            password_hash="hashed_password_123",
            first_name="Alice",
            last_name="Johnson",
            created_at=datetime.utcnow()
        )
        await user1.save()
        
        user2 = User(
            email="bob@example.com",
            password_hash="hashed_password_456",
            first_name="Bob",
            last_name="Smith",
            created_at=datetime.utcnow()
        )
        await user2.save()
        
        print(f"Created users: {user1.full_name}, {user2.full_name}")
        
        # Create products
        product1 = Product(
            name="Laptop",
            description="Gaming laptop with RTX 4080",
            price=1599.99,
            stock_quantity=10,
            created_at=datetime.utcnow()
        )
        await product1.save()
        
        product2 = Product(
            name="Mouse",
            description="Wireless gaming mouse",
            price=79.99,
            stock_quantity=50,
            created_at=datetime.utcnow()
        )
        await product2.save()
        
        print(f"Created products: {product1.name}, {product2.name}")
        
        # Create order
        order = Order(
            user_id=user1.id,
            total_amount=1679.98,
            status="pending",
            created_at=datetime.utcnow()
        )
        await order.save()
        
        print(f"Created order for user {user1.email}")
        
        # Query operations
        print("\n--- Query Operations ---")
        
        # Find by ID
        found_user = await User.find_by_id(1)
        print(f"Found user by ID: {found_user.email if found_user else 'Not found'}")
        
        # Find by email
        found_user = await User.find_by_email("bob@example.com")
        print(f"Found user by email: {found_user.full_name if found_user else 'Not found'}")
        
        # Find all products
        all_products = await Product.find_all()
        print(f"All products: {[p.name for p in all_products]}")
        
        # Find products with condition
        expensive_products = await Product.find_where(price=1599.99)
        print(f"Expensive products: {[p.name for p in expensive_products]}")
        
        # Update operations
        print("\n--- Update Operations ---")
        
        product1.price = 1499.99
        await product1.save()
        print(f"Updated {product1.name} price to {product1.price}")
        
        # Stock update
        await product2.update_stock(-5)
        print(f"Updated {product2.name} stock to {product2.stock_quantity}")
        
        # Query builder example
        print("\n--- Query Builder ---")
        
        async with pool.connection() as conn:
            query = QueryBuilder("users") \
                .select("email", "first_name", "last_name") \
                .where("is_active = ?", True) \
                .order_by("created_at", "DESC") \
                .limit(10)
            
            sql, params = query.build()
            print(f"Built query: {sql}")
            
            results = await conn.execute(sql, params)
            print(f"Query results: {results}")
    
    finally:
        await pool.close_all()

# Run ORM demo
asyncio.run(orm_demo())

# =============================================================================
# 3. MIGRATION SYSTEM
# =============================================================================

print("\n=== Migration System ===")

@dataclass
class Migration:
    """Database migration"""
    version: str
    name: str
    up_sql: str
    down_sql: str
    applied_at: Optional[datetime] = None
    
    def get_filename(self) -> str:
        """Get migration filename"""
        return f"{self.version}_{self.name}.py"

class MigrationManager:
    """Database migration manager"""
    
    def __init__(self, connection_pool: ConnectionPool):
        self.connection_pool = connection_pool
        self.migrations: Dict[str, Migration] = {}
        self.applied_migrations: Set[str] = set()
    
    async def initialize(self):
        """Initialize migration system"""
        async with self.connection_pool.connection() as conn:
            # Create migrations table
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS migrations (
                    version VARCHAR(255) PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    applied_at TIMESTAMP NOT NULL
                )
            """)
            
            # Load applied migrations
            results = await conn.execute("SELECT version FROM migrations")
            self.applied_migrations = {row["version"] for row in results}
            
            print(f"🔄 Migration system initialized ({len(self.applied_migrations)} applied)")
    
    def add_migration(self, migration: Migration):
        """Add migration"""
        self.migrations[migration.version] = migration
        print(f"📝 Migration added: {migration.version}_{migration.name}")
    
    async def run_migrations(self):
        """Run pending migrations"""
        pending = self.get_pending_migrations()
        
        if not pending:
            print("✅ No pending migrations")
            return
        
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                for migration in pending:
                    print(f"🔄 Applying migration: {migration.version}_{migration.name}")
                    
                    # Execute UP migration
                    for sql_statement in migration.up_sql.split(';'):
                        sql_statement = sql_statement.strip()
                        if sql_statement:
                            await conn.execute(sql_statement)
                    
                    # Record migration as applied
                    await conn.execute(
                        "INSERT INTO migrations (version, name, applied_at) VALUES (?, ?, ?)",
                        (migration.version, migration.name, datetime.utcnow())
                    )
                    
                    self.applied_migrations.add(migration.version)
                    print(f"✅ Migration applied: {migration.version}_{migration.name}")
                
                await conn.commit()
                print(f"🎉 Applied {len(pending)} migrations successfully")
                
            except Exception as e:
                await conn.rollback()
                print(f"❌ Migration failed: {str(e)}")
                raise
    
    async def rollback_migration(self, version: str):
        """Rollback specific migration"""
        if version not in self.applied_migrations:
            print(f"⚠️ Migration {version} is not applied")
            return
        
        migration = self.migrations.get(version)
        if not migration:
            print(f"❌ Migration {version} not found")
            return
        
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                print(f"🔄 Rolling back migration: {migration.version}_{migration.name}")
                
                # Execute DOWN migration
                for sql_statement in migration.down_sql.split(';'):
                    sql_statement = sql_statement.strip()
                    if sql_statement:
                        await conn.execute(sql_statement)
                
                # Remove migration record
                await conn.execute("DELETE FROM migrations WHERE version = ?", (version,))
                
                self.applied_migrations.discard(version)
                await conn.commit()
                
                print(f"✅ Migration rolled back: {migration.version}_{migration.name}")
                
            except Exception as e:
                await conn.rollback()
                print(f"❌ Rollback failed: {str(e)}")
                raise
    
    def get_pending_migrations(self) -> List[Migration]:
        """Get pending migrations in order"""
        pending = []
        
        for version in sorted(self.migrations.keys()):
            if version not in self.applied_migrations:
                pending.append(self.migrations[version])
        
        return pending
    
    def get_migration_status(self) -> Dict[str, Any]:
        """Get migration status"""
        total_migrations = len(self.migrations)
        applied_count = len(self.applied_migrations)
        pending_count = total_migrations - applied_count
        
        return {
            "total": total_migrations,
            "applied": applied_count,
            "pending": pending_count,
            "pending_migrations": [m.version for m in self.get_pending_migrations()]
        }

# Sample migrations
def create_sample_migrations() -> List[Migration]:
    """Create sample migrations"""
    migrations = []
    
    # Migration 001: Create users table
    migrations.append(Migration(
        version="001",
        name="create_users_table",
        up_sql="""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                is_active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        down_sql="DROP TABLE users"
    ))
    
    # Migration 002: Create products table
    migrations.append(Migration(
        version="002",
        name="create_products_table",
        up_sql="""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                price REAL NOT NULL,
                stock_quantity INTEGER DEFAULT 0,
                is_active BOOLEAN DEFAULT true,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """,
        down_sql="DROP TABLE products"
    ))
    
    # Migration 003: Add category support
    migrations.append(Migration(
        version="003",
        name="add_category_to_products",
        up_sql="""
            CREATE TABLE categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            
            ALTER TABLE products ADD COLUMN category_id INTEGER;
        """,
        down_sql="""
            ALTER TABLE products DROP COLUMN category_id;
            DROP TABLE categories;
        """
    ))
    
    # Migration 004: Add indexes for performance
    migrations.append(Migration(
        version="004",
        name="add_performance_indexes",
        up_sql="""
            CREATE INDEX idx_users_email ON users(email);
            CREATE INDEX idx_products_category ON products(category_id);
            CREATE INDEX idx_products_price ON products(price);
        """,
        down_sql="""
            DROP INDEX idx_users_email;
            DROP INDEX idx_products_category;
            DROP INDEX idx_products_price;
        """
    ))
    
    return migrations

# =============================================================================
# 4. TRANSACTION MANAGEMENT
# =============================================================================

print("\n=== Transaction Management ===")

class TransactionManager:
    """Database transaction manager"""
    
    def __init__(self, connection_pool: ConnectionPool):
        self.connection_pool = connection_pool
    
    @asynccontextmanager
    async def transaction(self):
        """Transaction context manager"""
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                yield conn
                await conn.commit()
                print("✅ Transaction committed successfully")
            except Exception as e:
                await conn.rollback()
                print(f"🔙 Transaction rolled back: {str(e)}")
                raise
    
    async def execute_in_transaction(self, operations: List[Callable]):
        """Execute multiple operations in a single transaction"""
        async with self.transaction() as conn:
            results = []
            
            for operation in operations:
                if asyncio.iscoroutinefunction(operation):
                    result = await operation(conn)
                else:
                    result = operation(conn)
                results.append(result)
            
            return results

class UnitOfWork:
    """Unit of Work pattern implementation"""
    
    def __init__(self, connection_pool: ConnectionPool):
        self.connection_pool = connection_pool
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []
        self._committed = False
    
    def register_new(self, obj):
        """Register new object"""
        self.new_objects.append(obj)
        print(f"📝 Registered new object: {obj.__class__.__name__}")
    
    def register_dirty(self, obj):
        """Register dirty (modified) object"""
        if obj not in self.dirty_objects:
            self.dirty_objects.append(obj)
            print(f"🔄 Registered dirty object: {obj.__class__.__name__}")
    
    def register_removed(self, obj):
        """Register removed object"""
        self.removed_objects.append(obj)
        # Remove from other lists if present
        if obj in self.new_objects:
            self.new_objects.remove(obj)
        if obj in self.dirty_objects:
            self.dirty_objects.remove(obj)
        print(f"🗑️ Registered removed object: {obj.__class__.__name__}")
    
    async def commit(self):
        """Commit all changes"""
        if self._committed:
            print("⚠️ Unit of work already committed")
            return
        
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                # Save new objects
                for obj in self.new_objects:
                    if hasattr(obj, 'save'):
                        await obj.save()
                
                # Save dirty objects
                for obj in self.dirty_objects:
                    if hasattr(obj, 'save'):
                        await obj.save()
                
                # Remove objects
                for obj in self.removed_objects:
                    if hasattr(obj, 'delete'):
                        await obj.delete()
                
                await conn.commit()
                self._committed = True
                
                print(f"✅ Unit of Work committed: {len(self.new_objects)} new, "
                      f"{len(self.dirty_objects)} updated, {len(self.removed_objects)} removed")
                
            except Exception as e:
                await conn.rollback()
                print(f"❌ Unit of Work failed: {str(e)}")
                raise
    
    async def rollback(self):
        """Rollback changes"""
        self.new_objects.clear()
        self.dirty_objects.clear()
        self.removed_objects.clear()
        self._committed = False
        print("🔙 Unit of Work rolled back")

# =============================================================================
# 5. PERFORMANCE OPTIMIZATION
# =============================================================================

print("\n=== Performance Optimization ===")

class QueryOptimizer:
    """Database query optimizer"""
    
    def __init__(self, connection_pool: ConnectionPool):
        self.connection_pool = connection_pool
        self.query_cache = {}
        self.execution_stats = defaultdict(list)
    
    async def analyze_query(self, sql: str, params: tuple = None):
        """Analyze query performance"""
        async with self.connection_pool.connection() as conn:
            # Get query plan (SQLite specific)
            explain_sql = f"EXPLAIN QUERY PLAN {sql}"
            
            start_time = time.time()
            
            try:
                plan = await conn.execute(explain_sql, params)
                execution_time = time.time() - start_time
                
                # Store execution stats
                query_hash = hashlib.md5(sql.encode()).hexdigest()
                self.execution_stats[query_hash].append({
                    "execution_time": execution_time,
                    "timestamp": datetime.utcnow(),
                    "plan": plan
                })
                
                return {
                    "sql": sql,
                    "execution_time": execution_time,
                    "plan": plan,
                    "optimization_suggestions": self._get_optimization_suggestions(sql, plan)
                }
                
            except Exception as e:
                return {
                    "sql": sql,
                    "error": str(e),
                    "optimization_suggestions": []
                }
    
    def _get_optimization_suggestions(self, sql: str, plan: List[dict]) -> List[str]:
        """Get optimization suggestions based on query plan"""
        suggestions = []
        
        sql_upper = sql.upper()
        
        # Check for table scans
        for step in plan:
            detail = step.get("detail", "").upper()
            
            if "SCAN TABLE" in detail and "USING INDEX" not in detail:
                table_name = self._extract_table_name(detail)
                suggestions.append(f"Consider adding an index to table '{table_name}'")
        
        # Check for missing WHERE clause on large operations
        if ("SELECT" in sql_upper and 
            "WHERE" not in sql_upper and 
            "LIMIT" not in sql_upper):
            suggestions.append("Consider adding WHERE clause to limit results")
        
        # Check for SELECT * usage
        if "SELECT *" in sql_upper:
            suggestions.append("Consider selecting only needed columns instead of SELECT *")
        
        # Check for OR conditions (suggest UNION)
        if " OR " in sql_upper and "WHERE" in sql_upper:
            suggestions.append("Consider using UNION instead of OR for better performance")
        
        return suggestions
    
    def _extract_table_name(self, detail: str) -> str:
        """Extract table name from query plan detail"""
        # Simple regex to extract table name
        import re
        match = re.search(r'TABLE (\w+)', detail)
        return match.group(1) if match else "unknown"
    
    def get_slow_queries(self, threshold_seconds: float = 1.0) -> List[dict]:
        """Get slow queries above threshold"""
        slow_queries = []
        
        for query_hash, stats in self.execution_stats.items():
            avg_time = sum(s["execution_time"] for s in stats) / len(stats)
            max_time = max(s["execution_time"] for s in stats)
            
            if avg_time > threshold_seconds:
                slow_queries.append({
                    "query_hash": query_hash,
                    "execution_count": len(stats),
                    "avg_execution_time": avg_time,
                    "max_execution_time": max_time,
                    "last_executed": max(s["timestamp"] for s in stats)
                })
        
        return sorted(slow_queries, key=lambda x: x["avg_execution_time"], reverse=True)

class CacheManager:
    """Query result caching"""
    
    def __init__(self, default_ttl: timedelta = timedelta(minutes=5)):
        self.cache = {}
        self.cache_stats = {"hits": 0, "misses": 0}
        self.default_ttl = default_ttl
    
    def _get_cache_key(self, sql: str, params: tuple = None) -> str:
        """Generate cache key"""
        key_data = f"{sql}:{params or ()}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def get(self, sql: str, params: tuple = None) -> Optional[Any]:
        """Get cached result"""
        cache_key = self._get_cache_key(sql, params)
        
        if cache_key in self.cache:
            cached_item = self.cache[cache_key]
            
            # Check if expired
            if datetime.utcnow() < cached_item["expires_at"]:
                self.cache_stats["hits"] += 1
                print(f"🎯 Cache hit for query: {sql[:50]}...")
                return cached_item["result"]
            else:
                # Remove expired item
                del self.cache[cache_key]
        
        self.cache_stats["misses"] += 1
        return None
    
    def set(self, sql: str, params: tuple, result: Any, ttl: timedelta = None):
        """Cache query result"""
        cache_key = self._get_cache_key(sql, params)
        ttl = ttl or self.default_ttl
        
        self.cache[cache_key] = {
            "result": result,
            "created_at": datetime.utcnow(),
            "expires_at": datetime.utcnow() + ttl
        }
        
        print(f"💾 Cached query result: {sql[:50]}... (TTL: {ttl})")
    
    def invalidate_pattern(self, pattern: str):
        """Invalidate cache entries matching pattern"""
        keys_to_remove = []
        
        for cache_key in self.cache:
            # Simple pattern matching (in production, use more sophisticated matching)
            if pattern.lower() in cache_key.lower():
                keys_to_remove.append(cache_key)
        
        for key in keys_to_remove:
            del self.cache[key]
        
        print(f"🗑️ Invalidated {len(keys_to_remove)} cache entries matching '{pattern}'")
    
    def clear(self):
        """Clear all cache"""
        count = len(self.cache)
        self.cache.clear()
        print(f"🧹 Cleared {count} cache entries")
    
    def get_stats(self) -> dict:
        """Get cache statistics"""
        total_requests = self.cache_stats["hits"] + self.cache_stats["misses"]
        hit_rate = (self.cache_stats["hits"] / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "total_entries": len(self.cache),
            "total_requests": total_requests,
            "hits": self.cache_stats["hits"],
            "misses": self.cache_stats["misses"],
            "hit_rate_percent": round(hit_rate, 2)
        }

class BatchProcessor:
    """Batch processing for database operations"""
    
    def __init__(self, connection_pool: ConnectionPool, batch_size: int = 1000):
        self.connection_pool = connection_pool
        self.batch_size = batch_size
    
    async def batch_insert(self, table_name: str, records: List[dict]) -> int:
        """Batch insert records"""
        if not records:
            return 0
        
        # Get column names from first record
        columns = list(records[0].keys())
        placeholders = ", ".join(["?" for _ in columns])
        sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        
        total_inserted = 0
        
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                for i in range(0, len(records), self.batch_size):
                    batch = records[i:i + self.batch_size]
                    
                    # Convert records to tuple list
                    params_list = [tuple(record[col] for col in columns) for record in batch]
                    
                    inserted = await conn.execute_many(sql, params_list)
                    total_inserted += inserted
                    
                    print(f"📥 Inserted batch {i//self.batch_size + 1}: {len(batch)} records")
                
                await conn.commit()
                print(f"✅ Batch insert completed: {total_inserted} total records")
                
                return total_inserted
                
            except Exception as e:
                await conn.rollback()
                print(f"❌ Batch insert failed: {str(e)}")
                raise
    
    async def batch_update(self, table_name: str, updates: List[dict], key_column: str) -> int:
        """Batch update records"""
        if not updates:
            return 0
        
        total_updated = 0
        
        async with self.connection_pool.connection() as conn:
            await conn.begin_transaction()
            
            try:
                for i in range(0, len(updates), self.batch_size):
                    batch = updates[i:i + self.batch_size]
                    
                    for record in batch:
                        # Build UPDATE query
                        set_columns = [col for col in record.keys() if col != key_column]
                        set_clause = ", ".join([f"{col} = ?" for col in set_columns])
                        
                        sql = f"UPDATE {table_name} SET {set_clause} WHERE {key_column} = ?"
                        params = [record[col] for col in set_columns] + [record[key_column]]
                        
                        updated = await conn.execute(sql, tuple(params))
                        if updated:
                            total_updated += updated
                    
                    print(f"🔄 Updated batch {i//self.batch_size + 1}: {len(batch)} records")
                
                await conn.commit()
                print(f"✅ Batch update completed: {total_updated} total records")
                
                return total_updated
                
            except Exception as e:
                await conn.rollback()
                print(f"❌ Batch update failed: {str(e)}")
                raise

# Comprehensive demonstration
print("Database operations comprehensive demo örnekleri:")

async def comprehensive_demo():
    # Setup connection pool
    pool = ConnectionPool("sqlite:///:memory:", DatabaseType.SQLITE, min_connections=2, max_connections=5)
    await pool.initialize()
    
    try:
        # 1. Migration system
        print("\n--- Migration System ---")
        migration_manager = MigrationManager(pool)
        await migration_manager.initialize()
        
        # Add sample migrations
        for migration in create_sample_migrations():
            migration_manager.add_migration(migration)
        
        # Run migrations
        await migration_manager.run_migrations()
        
        # Check status
        status = migration_manager.get_migration_status()
        print(f"Migration status: {status}")
        
        # 2. Transaction management
        print("\n--- Transaction Management ---")
        transaction_manager = TransactionManager(pool)
        
        # Unit of Work example
        uow = UnitOfWork(pool)
        
        # Set connection pool for models
        Model.set_connection_pool(pool)
        
        # Create test data using UnitOfWork
        user1 = User(
            email="alice@example.com",
            password_hash="hash123",
            first_name="Alice",
            last_name="Johnson",
            created_at=datetime.utcnow()
        )
        
        user2 = User(
            email="bob@example.com",
            password_hash="hash456",
            first_name="Bob",
            last_name="Smith",
            created_at=datetime.utcnow()
        )
        
        uow.register_new(user1)
        uow.register_new(user2)
        await uow.commit()
        
        # 3. Performance optimization
        print("\n--- Performance Optimization ---")
        
        optimizer = QueryOptimizer(pool)
        cache_manager = CacheManager()
        batch_processor = BatchProcessor(pool)
        
        # Analyze query performance
        test_queries = [
            "SELECT * FROM users",
            "SELECT * FROM users WHERE email = ?",
            "SELECT u.*, p.* FROM users u JOIN products p ON u.id = p.id"
        ]
        
        for sql in test_queries:
            analysis = await optimizer.analyze_query(sql)
            print(f"\nQuery: {sql}")
            print(f"Execution time: {analysis.get('execution_time', 'N/A')}")
            print(f"Suggestions: {analysis.get('optimization_suggestions', [])}")
        
        # Cache demonstration
        async with pool.connection() as conn:
            # First query - cache miss
            sql = "SELECT * FROM users WHERE is_active = ?"
            params = (True,)
            
            cached_result = cache_manager.get(sql, params)
            if cached_result is None:
                result = await conn.execute(sql, params)
                cache_manager.set(sql, params, result)
            else:
                result = cached_result
            
            print(f"First query result: {len(result)} users")
            
            # Second query - cache hit
            cached_result = cache_manager.get(sql, params)
            if cached_result is not None:
                print("Second query served from cache")
        
        # Cache stats
        stats = cache_manager.get_stats()
        print(f"Cache stats: {stats}")
        
        # Batch processing demonstration
        print("\n--- Batch Processing ---")
        
        # Generate test data
        test_products = []
        for i in range(100):
            test_products.append({
                "name": f"Product {i+1}",
                "description": f"Description for product {i+1}",
                "price": round(10.0 + i * 0.5, 2),
                "stock_quantity": 50 + i,
                "is_active": True,
                "created_at": datetime.utcnow()
            })
        
        # Batch insert
        inserted_count = await batch_processor.batch_insert("products", test_products)
        print(f"Batch inserted {inserted_count} products")
        
        # Batch update
        updates = []
        for i in range(1, 21):  # Update first 20 products
            updates.append({
                "id": i,
                "price": 15.99,
                "stock_quantity": 100
            })
        
        updated_count = await batch_processor.batch_update("products", updates, "id")
        print(f"Batch updated {updated_count} products")
        
        # Performance monitoring
        slow_queries = optimizer.get_slow_queries(0.001)  # Very low threshold for demo
        print(f"Detected {len(slow_queries)} slow queries")
        
    finally:
        await pool.close_all()

# Run comprehensive demo
asyncio.run(comprehensive_demo())

print("\n" + "="*60)
print("VERİTABANI İŞLEMLERİ TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Database Abstraction Layer (Connection, Table, Column)")
print("2. Connection Pooling & Management")
print("3. ORM Implementation (Models, Queries)")
print("4. Query Builder & Advanced Queries")
print("5. Migration System & Schema Management")
print("6. Transaction Management & Unit of Work")
print("7. Performance Optimization & Query Analysis")
print("8. Caching System & Cache Management")
print("9. Batch Processing & Bulk Operations")

print("\nBir sonraki dosya: test_stratejileri.py")