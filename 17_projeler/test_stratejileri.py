"""
Python Test Stratejileri - Comprehensive Guide
Unit Testing, Integration Testing, Performance Testing, Test Automation

Bu dosyada modern test stratejileri, unit testing, integration testing,
performance testing, test automation ve CI/CD test pipeline konuları incelenecek.
"""

import asyncio
import unittest
import pytest
from unittest.mock import Mock, MagicMock, patch, AsyncMock
import time
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Callable, Generator
from dataclasses import dataclass
from enum import Enum
import uuid
import tempfile
import os
from contextlib import contextmanager
import statistics
import threading
from collections import defaultdict
import random

# =============================================================================
# 1. UNIT TESTING FRAMEWORK
# =============================================================================

print("=== Unit Testing Framework ===")

class TestResult(Enum):
    """Test result enumeration"""
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
    ERROR = "ERROR"

@dataclass
class TestCase:
    """Test case representation"""
    name: str
    description: str
    test_function: Callable
    setup_function: Optional[Callable] = None
    teardown_function: Optional[Callable] = None
    tags: List[str] = None
    timeout: float = 30.0
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []

@dataclass
class TestExecution:
    """Test execution result"""
    test_name: str
    result: TestResult
    execution_time: float
    error_message: Optional[str] = None
    stack_trace: Optional[str] = None
    assertions_count: int = 0
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "test_name": self.test_name,
            "result": self.result.value,
            "execution_time": self.execution_time,
            "error_message": self.error_message,
            "stack_trace": self.stack_trace,
            "assertions_count": self.assertions_count
        }

class AssertionError(Exception):
    """Custom assertion error"""
    pass

class TestAssertions:
    """Test assertion utilities"""
    
    def __init__(self):
        self.assertion_count = 0
    
    def assert_equal(self, actual: Any, expected: Any, message: str = ""):
        """Assert that two values are equal"""
        self.assertion_count += 1
        if actual != expected:
            error_msg = f"Expected {expected}, but got {actual}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_not_equal(self, actual: Any, expected: Any, message: str = ""):
        """Assert that two values are not equal"""
        self.assertion_count += 1
        if actual == expected:
            error_msg = f"Expected values to be different, but both are {actual}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_true(self, condition: bool, message: str = ""):
        """Assert that condition is true"""
        self.assertion_count += 1
        if not condition:
            error_msg = "Expected True, but got False"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_false(self, condition: bool, message: str = ""):
        """Assert that condition is false"""
        self.assertion_count += 1
        if condition:
            error_msg = "Expected False, but got True"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_none(self, value: Any, message: str = ""):
        """Assert that value is None"""
        self.assertion_count += 1
        if value is not None:
            error_msg = f"Expected None, but got {value}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_not_none(self, value: Any, message: str = ""):
        """Assert that value is not None"""
        self.assertion_count += 1
        if value is None:
            error_msg = "Expected not None, but got None"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_in(self, item: Any, container: Any, message: str = ""):
        """Assert that item is in container"""
        self.assertion_count += 1
        if item not in container:
            error_msg = f"Expected {item} to be in {container}"
            if message:
                error_msg = f"{message}: {error_msg}"
            raise AssertionError(error_msg)
    
    def assert_raises(self, exception_class: type, callable_obj: Callable, *args, **kwargs):
        """Assert that callable raises specified exception"""
        self.assertion_count += 1
        try:
            callable_obj(*args, **kwargs)
            raise AssertionError(f"Expected {exception_class.__name__} to be raised")
        except exception_class:
            # Expected exception was raised
            pass
        except Exception as e:
            raise AssertionError(f"Expected {exception_class.__name__}, but got {type(e).__name__}: {str(e)}")

class TestRunner:
    """Test runner implementation"""
    
    def __init__(self):
        self.test_cases: List[TestCase] = []
        self.results: List[TestExecution] = []
        self.setup_functions: List[Callable] = []
        self.teardown_functions: List[Callable] = []
        self.parallel_execution = False
    
    def add_test(self, test_case: TestCase):
        """Add test case"""
        self.test_cases.append(test_case)
        print(f"📝 Test registered: {test_case.name}")
    
    def add_setup(self, setup_function: Callable):
        """Add global setup function"""
        self.setup_functions.append(setup_function)
        print(f"🔧 Global setup registered: {setup_function.__name__}")
    
    def add_teardown(self, teardown_function: Callable):
        """Add global teardown function"""
        self.teardown_functions.append(teardown_function)
        print(f"🧹 Global teardown registered: {teardown_function.__name__}")
    
    async def run_tests(self, filter_tags: List[str] = None) -> Dict[str, Any]:
        """Run all tests"""
        print(f"\n🚀 Starting test execution ({len(self.test_cases)} tests)")
        
        # Filter tests by tags if specified
        tests_to_run = self.test_cases
        if filter_tags:
            tests_to_run = [
                test for test in self.test_cases
                if any(tag in test.tags for tag in filter_tags)
            ]
        
        # Run global setup
        for setup_func in self.setup_functions:
            try:
                if asyncio.iscoroutinefunction(setup_func):
                    await setup_func()
                else:
                    setup_func()
            except Exception as e:
                print(f"❌ Global setup failed: {str(e)}")
                return self._create_summary()
        
        # Run tests
        if self.parallel_execution:
            await self._run_tests_parallel(tests_to_run)
        else:
            await self._run_tests_sequential(tests_to_run)
        
        # Run global teardown
        for teardown_func in self.teardown_functions:
            try:
                if asyncio.iscoroutinefunction(teardown_func):
                    await teardown_func()
                else:
                    teardown_func()
            except Exception as e:
                print(f"⚠️ Global teardown error: {str(e)}")
        
        # Create summary
        summary = self._create_summary()
        self._print_summary(summary)
        
        return summary
    
    async def _run_tests_sequential(self, tests: List[TestCase]):
        """Run tests sequentially"""
        for test_case in tests:
            execution = await self._execute_test(test_case)
            self.results.append(execution)
    
    async def _run_tests_parallel(self, tests: List[TestCase]):
        """Run tests in parallel"""
        tasks = []
        for test_case in tests:
            task = asyncio.create_task(self._execute_test(test_case))
            tasks.append(task)
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, TestExecution):
                self.results.append(result)
            else:
                # Handle execution exception
                error_execution = TestExecution(
                    test_name="unknown",
                    result=TestResult.ERROR,
                    execution_time=0.0,
                    error_message=str(result)
                )
                self.results.append(error_execution)
    
    async def _execute_test(self, test_case: TestCase) -> TestExecution:
        """Execute individual test"""
        start_time = time.time()
        assertions = TestAssertions()
        
        try:
            # Run test-specific setup
            if test_case.setup_function:
                if asyncio.iscoroutinefunction(test_case.setup_function):
                    await test_case.setup_function()
                else:
                    test_case.setup_function()
            
            # Execute test with timeout
            try:
                if asyncio.iscoroutinefunction(test_case.test_function):
                    await asyncio.wait_for(
                        test_case.test_function(assertions),
                        timeout=test_case.timeout
                    )
                else:
                    test_case.test_function(assertions)
                
                result = TestResult.PASSED
                error_message = None
                stack_trace = None
                
            except asyncio.TimeoutError:
                result = TestResult.ERROR
                error_message = f"Test timed out after {test_case.timeout} seconds"
                stack_trace = None
            
            except AssertionError as e:
                result = TestResult.FAILED
                error_message = str(e)
                stack_trace = None
            
            except Exception as e:
                result = TestResult.ERROR
                error_message = str(e)
                import traceback
                stack_trace = traceback.format_exc()
            
            # Run test-specific teardown
            if test_case.teardown_function:
                try:
                    if asyncio.iscoroutinefunction(test_case.teardown_function):
                        await test_case.teardown_function()
                    else:
                        test_case.teardown_function()
                except Exception as e:
                    print(f"⚠️ Teardown error for {test_case.name}: {str(e)}")
            
            execution_time = time.time() - start_time
            
            execution = TestExecution(
                test_name=test_case.name,
                result=result,
                execution_time=execution_time,
                error_message=error_message,
                stack_trace=stack_trace,
                assertions_count=assertions.assertion_count
            )
            
            # Print result
            status_icon = {
                TestResult.PASSED: "✅",
                TestResult.FAILED: "❌", 
                TestResult.SKIPPED: "⏭️",
                TestResult.ERROR: "💥"
            }
            
            print(f"{status_icon[result]} {test_case.name} ({execution_time:.3f}s)")
            if error_message:
                print(f"    {error_message}")
            
            return execution
            
        except Exception as e:
            execution_time = time.time() - start_time
            return TestExecution(
                test_name=test_case.name,
                result=TestResult.ERROR,
                execution_time=execution_time,
                error_message=f"Test execution error: {str(e)}"
            )
    
    def _create_summary(self) -> Dict[str, Any]:
        """Create test execution summary"""
        total_tests = len(self.results)
        if total_tests == 0:
            return {"total": 0, "passed": 0, "failed": 0, "errors": 0, "skipped": 0}
        
        passed = sum(1 for r in self.results if r.result == TestResult.PASSED)
        failed = sum(1 for r in self.results if r.result == TestResult.FAILED)
        errors = sum(1 for r in self.results if r.result == TestResult.ERROR)
        skipped = sum(1 for r in self.results if r.result == TestResult.SKIPPED)
        
        total_time = sum(r.execution_time for r in self.results)
        avg_time = total_time / total_tests
        
        return {
            "total": total_tests,
            "passed": passed,
            "failed": failed,
            "errors": errors,
            "skipped": skipped,
            "success_rate": (passed / total_tests) * 100 if total_tests > 0 else 0,
            "total_execution_time": total_time,
            "average_execution_time": avg_time,
            "results": [r.to_dict() for r in self.results]
        }
    
    def _print_summary(self, summary: Dict[str, Any]):
        """Print test summary"""
        print(f"\n{'='*60}")
        print("TEST EXECUTION SUMMARY")
        print(f"{'='*60}")
        print(f"Total Tests: {summary['total']}")
        print(f"✅ Passed: {summary['passed']}")
        print(f"❌ Failed: {summary['failed']}")
        print(f"💥 Errors: {summary['errors']}")
        print(f"⏭️ Skipped: {summary['skipped']}")
        print(f"Success Rate: {summary['success_rate']:.1f}%")
        print(f"Total Time: {summary['total_execution_time']:.3f}s")
        print(f"Average Time: {summary['average_execution_time']:.3f}s")

# Sample classes to test
class Calculator:
    """Simple calculator for testing"""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """Calculate power"""
        return base ** exponent

class UserService:
    """User service for testing"""
    
    def __init__(self):
        self.users = {}
        self.next_id = 1
    
    def create_user(self, email: str, name: str) -> dict:
        """Create new user"""
        if not email or '@' not in email:
            raise ValueError("Invalid email")
        
        if email in [user['email'] for user in self.users.values()]:
            raise ValueError("Email already exists")
        
        user_id = self.next_id
        self.next_id += 1
        
        user = {
            "id": user_id,
            "email": email,
            "name": name,
            "created_at": datetime.utcnow()
        }
        
        self.users[user_id] = user
        return user
    
    def get_user(self, user_id: int) -> Optional[dict]:
        """Get user by ID"""
        return self.users.get(user_id)
    
    def update_user(self, user_id: int, **updates) -> Optional[dict]:
        """Update user"""
        if user_id not in self.users:
            return None
        
        self.users[user_id].update(updates)
        return self.users[user_id]
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user"""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

# Unit test demonstration
print("Unit testing framework örnekleri:")

async def unit_testing_demo():
    # Create test runner
    runner = TestRunner()
    
    # Calculator tests
    def test_calculator_add(assertions: TestAssertions):
        """Test calculator addition"""
        calc = Calculator()
        result = calc.add(2, 3)
        assertions.assert_equal(result, 5, "Addition should work correctly")
    
    def test_calculator_divide_by_zero(assertions: TestAssertions):
        """Test division by zero raises error"""
        calc = Calculator()
        assertions.assert_raises(ValueError, calc.divide, 10, 0)
    
    async def test_calculator_power(assertions: TestAssertions):
        """Test calculator power function"""
        calc = Calculator()
        result = calc.power(2, 3)
        assertions.assert_equal(result, 8, "2^3 should equal 8")
        
        # Simulate async operation
        await asyncio.sleep(0.1)
        result = calc.power(5, 2)
        assertions.assert_equal(result, 25, "5^2 should equal 25")
    
    # User service tests
    def test_user_service_create_user(assertions: TestAssertions):
        """Test user creation"""
        service = UserService()
        user = service.create_user("alice@example.com", "Alice Johnson")
        
        assertions.assert_equal(user["email"], "alice@example.com")
        assertions.assert_equal(user["name"], "Alice Johnson")
        assertions.assert_not_none(user["id"])
        assertions.assert_not_none(user["created_at"])
    
    def test_user_service_invalid_email(assertions: TestAssertions):
        """Test invalid email handling"""
        service = UserService()
        assertions.assert_raises(ValueError, service.create_user, "invalid-email", "Test User")
    
    def test_user_service_duplicate_email(assertions: TestAssertions):
        """Test duplicate email handling"""
        service = UserService()
        service.create_user("test@example.com", "User 1")
        assertions.assert_raises(ValueError, service.create_user, "test@example.com", "User 2")
    
    def test_user_service_crud_operations(assertions: TestAssertions):
        """Test CRUD operations"""
        service = UserService()
        
        # Create
        user = service.create_user("bob@example.com", "Bob Smith")
        user_id = user["id"]
        
        # Read
        retrieved_user = service.get_user(user_id)
        assertions.assert_not_none(retrieved_user)
        assertions.assert_equal(retrieved_user["email"], "bob@example.com")
        
        # Update
        updated_user = service.update_user(user_id, name="Robert Smith")
        assertions.assert_equal(updated_user["name"], "Robert Smith")
        
        # Delete
        deleted = service.delete_user(user_id)
        assertions.assert_true(deleted)
        
        # Verify deletion
        deleted_user = service.get_user(user_id)
        assertions.assert_none(deleted_user)
    
    # Register tests
    runner.add_test(TestCase(
        name="test_calculator_add",
        description="Test basic addition functionality",
        test_function=test_calculator_add,
        tags=["calculator", "basic"]
    ))
    
    runner.add_test(TestCase(
        name="test_calculator_divide_by_zero",
        description="Test division by zero error handling",
        test_function=test_calculator_divide_by_zero,
        tags=["calculator", "error_handling"]
    ))
    
    runner.add_test(TestCase(
        name="test_calculator_power",
        description="Test power calculation with async operations",
        test_function=test_calculator_power,
        tags=["calculator", "async"]
    ))
    
    runner.add_test(TestCase(
        name="test_user_service_create_user",
        description="Test user creation functionality",
        test_function=test_user_service_create_user,
        tags=["user_service", "create"]
    ))
    
    runner.add_test(TestCase(
        name="test_user_service_invalid_email", 
        description="Test invalid email validation",
        test_function=test_user_service_invalid_email,
        tags=["user_service", "validation"]
    ))
    
    runner.add_test(TestCase(
        name="test_user_service_duplicate_email",
        description="Test duplicate email handling",
        test_function=test_user_service_duplicate_email,
        tags=["user_service", "validation"]
    ))
    
    runner.add_test(TestCase(
        name="test_user_service_crud_operations",
        description="Test complete CRUD operations",
        test_function=test_user_service_crud_operations,
        tags=["user_service", "crud"]
    ))
    
    # Run all tests
    summary = await runner.run_tests()
    
    # Run filtered tests
    print(f"\n{'-'*40}")
    print("Running only calculator tests:")
    runner.results.clear()  # Clear previous results
    await runner.run_tests(filter_tags=["calculator"])

# Run unit testing demo
asyncio.run(unit_testing_demo())

# =============================================================================
# 2. INTEGRATION TESTING
# =============================================================================

print("\n=== Integration Testing ===")

class DatabaseMock:
    """Mock database for testing"""
    
    def __init__(self):
        self.tables = defaultdict(dict)
        self.connected = False
        self.transaction_active = False
    
    async def connect(self):
        """Mock database connection"""
        await asyncio.sleep(0.01)  # Simulate connection time
        self.connected = True
        return True
    
    async def disconnect(self):
        """Mock database disconnection"""
        self.connected = False
    
    async def begin_transaction(self):
        """Mock transaction begin"""
        if not self.connected:
            raise RuntimeError("Not connected")
        self.transaction_active = True
    
    async def commit(self):
        """Mock transaction commit"""
        self.transaction_active = False
    
    async def rollback(self):
        """Mock transaction rollback"""
        self.transaction_active = False
    
    async def execute(self, query: str, params: tuple = None) -> Any:
        """Mock query execution"""
        if not self.connected:
            raise RuntimeError("Not connected")
        
        # Simulate query processing time
        await asyncio.sleep(0.001)
        
        # Simple query parsing for demo
        if query.startswith("INSERT"):
            # Mock insert
            table_name = "test_table"  # Simplified
            record_id = len(self.tables[table_name]) + 1
            self.tables[table_name][record_id] = {"id": record_id, "data": params}
            return record_id
        
        elif query.startswith("SELECT"):
            # Mock select
            table_name = "test_table"
            return list(self.tables[table_name].values())
        
        elif query.startswith("UPDATE"):
            # Mock update
            return 1  # Affected rows
        
        elif query.startswith("DELETE"):
            # Mock delete
            return 1  # Affected rows
        
        return []

class HTTPClientMock:
    """Mock HTTP client for testing"""
    
    def __init__(self):
        self.requests = []
        self.responses = {}
    
    def set_response(self, url: str, method: str, response: dict):
        """Set mock response for URL and method"""
        key = f"{method.upper()} {url}"
        self.responses[key] = response
    
    async def request(self, method: str, url: str, **kwargs) -> dict:
        """Mock HTTP request"""
        # Record request
        self.requests.append({
            "method": method.upper(),
            "url": url,
            "kwargs": kwargs,
            "timestamp": datetime.utcnow()
        })
        
        # Simulate network delay
        await asyncio.sleep(0.01)
        
        # Return mock response
        key = f"{method.upper()} {url}"
        if key in self.responses:
            return self.responses[key]
        else:
            return {
                "status_code": 404,
                "body": {"error": "Not found"}
            }

class IntegrationTestService:
    """Service for integration testing"""
    
    def __init__(self, database: DatabaseMock, http_client: HTTPClientMock):
        self.database = database
        self.http_client = http_client
    
    async def create_user_with_profile(self, user_data: dict) -> dict:
        """Create user and fetch profile from external service"""
        # Connect to database
        await self.database.connect()
        
        try:
            await self.database.begin_transaction()
            
            # Insert user
            user_id = await self.database.execute(
                "INSERT INTO users (email, name) VALUES (?, ?)",
                (user_data["email"], user_data["name"])
            )
            
            # Fetch additional profile data from external service
            profile_response = await self.http_client.request(
                "GET", 
                f"https://api.example.com/profiles/{user_data['email']}"
            )
            
            if profile_response["status_code"] == 200:
                profile_data = profile_response["body"]
                
                # Store profile data
                await self.database.execute(
                    "INSERT INTO profiles (user_id, data) VALUES (?, ?)",
                    (user_id, json.dumps(profile_data))
                )
            
            await self.database.commit()
            
            return {
                "user_id": user_id,
                "email": user_data["email"],
                "name": user_data["name"],
                "profile": profile_data if profile_response["status_code"] == 200 else None
            }
            
        except Exception as e:
            await self.database.rollback()
            raise
        finally:
            await self.database.disconnect()

class IntegrationTestRunner:
    """Integration test runner"""
    
    def __init__(self):
        self.setup_functions = []
        self.teardown_functions = []
        self.test_functions = []
    
    def setup(self, func: Callable):
        """Register setup function"""
        self.setup_functions.append(func)
        return func
    
    def teardown(self, func: Callable):
        """Register teardown function"""
        self.teardown_functions.append(func)
        return func
    
    def test(self, name: str, description: str = ""):
        """Register test function"""
        def decorator(func: Callable):
            self.test_functions.append({
                "name": name,
                "description": description,
                "function": func
            })
            return func
        return decorator
    
    async def run_tests(self) -> Dict[str, Any]:
        """Run integration tests"""
        print(f"\n🔧 Starting integration tests ({len(self.test_functions)} tests)")
        
        results = []
        
        # Run setup
        for setup_func in self.setup_functions:
            try:
                if asyncio.iscoroutinefunction(setup_func):
                    await setup_func()
                else:
                    setup_func()
            except Exception as e:
                print(f"❌ Setup failed: {str(e)}")
                return {"error": "Setup failed", "message": str(e)}
        
        # Run tests
        for test_info in self.test_functions:
            start_time = time.time()
            
            try:
                if asyncio.iscoroutinefunction(test_info["function"]):
                    await test_info["function"]()
                else:
                    test_info["function"]()
                
                execution_time = time.time() - start_time
                result = {
                    "name": test_info["name"],
                    "status": "PASSED",
                    "execution_time": execution_time,
                    "error": None
                }
                
                print(f"✅ {test_info['name']} ({execution_time:.3f}s)")
                
            except Exception as e:
                execution_time = time.time() - start_time
                result = {
                    "name": test_info["name"],
                    "status": "FAILED",
                    "execution_time": execution_time,
                    "error": str(e)
                }
                
                print(f"❌ {test_info['name']} ({execution_time:.3f}s): {str(e)}")
            
            results.append(result)
        
        # Run teardown
        for teardown_func in self.teardown_functions:
            try:
                if asyncio.iscoroutinefunction(teardown_func):
                    await teardown_func()
                else:
                    teardown_func()
            except Exception as e:
                print(f"⚠️ Teardown error: {str(e)}")
        
        # Summary
        passed = sum(1 for r in results if r["status"] == "PASSED")
        failed = len(results) - passed
        total_time = sum(r["execution_time"] for r in results)
        
        summary = {
            "total_tests": len(results),
            "passed": passed,
            "failed": failed,
            "success_rate": (passed / len(results)) * 100 if results else 0,
            "total_execution_time": total_time,
            "results": results
        }
        
        print(f"\n🏁 Integration Tests Summary:")
        print(f"   Total: {summary['total_tests']}")
        print(f"   ✅ Passed: {summary['passed']}")
        print(f"   ❌ Failed: {summary['failed']}")
        print(f"   Success Rate: {summary['success_rate']:.1f}%")
        
        return summary

# Integration test demonstration
print("Integration testing örnekleri:")

async def integration_testing_demo():
    # Setup test runner
    runner = IntegrationTestRunner()
    
    # Test dependencies
    database_mock = DatabaseMock()
    http_client_mock = HTTPClientMock()
    test_service = IntegrationTestService(database_mock, http_client_mock)
    
    # Setup mock responses
    http_client_mock.set_response(
        "https://api.example.com/profiles/alice@example.com",
        "GET",
        {
            "status_code": 200,
            "body": {
                "avatar_url": "https://example.com/avatars/alice.jpg",
                "bio": "Software Engineer",
                "location": "New York"
            }
        }
    )
    
    @runner.setup
    async def setup_integration_tests():
        """Setup integration test environment"""
        print("🔧 Setting up integration test environment...")
        # Any global setup can go here
    
    @runner.teardown
    async def teardown_integration_tests():
        """Cleanup integration test environment"""
        print("🧹 Cleaning up integration test environment...")
        # Any global cleanup can go here
    
    @runner.test("test_user_creation_with_profile", "Test creating user with external profile data")
    async def test_user_creation_with_profile():
        """Test user creation with profile integration"""
        user_data = {
            "email": "alice@example.com",
            "name": "Alice Johnson"
        }
        
        result = await test_service.create_user_with_profile(user_data)
        
        # Verify result
        assert result["email"] == "alice@example.com"
        assert result["name"] == "Alice Johnson"
        assert result["user_id"] is not None
        assert result["profile"] is not None
        assert result["profile"]["bio"] == "Software Engineer"
        
        # Verify HTTP request was made
        assert len(http_client_mock.requests) == 1
        request = http_client_mock.requests[0]
        assert request["method"] == "GET"
        assert "alice@example.com" in request["url"]
    
    @runner.test("test_user_creation_without_profile", "Test user creation when profile service is unavailable")
    async def test_user_creation_without_profile():
        """Test user creation when external service fails"""
        # Setup service to return error
        http_client_mock.set_response(
            "https://api.example.com/profiles/bob@example.com",
            "GET",
            {"status_code": 500, "body": {"error": "Internal server error"}}
        )
        
        user_data = {
            "email": "bob@example.com", 
            "name": "Bob Smith"
        }
        
        result = await test_service.create_user_with_profile(user_data)
        
        # Should still create user, but without profile
        assert result["email"] == "bob@example.com"
        assert result["name"] == "Bob Smith"
        assert result["user_id"] is not None
        assert result["profile"] is None
    
    @runner.test("test_database_transaction_rollback", "Test database transaction rollback on error")
    async def test_database_transaction_rollback():
        """Test that database transactions are properly rolled back on errors"""
        # This test would verify that if an error occurs during the process,
        # the database transaction is properly rolled back
        
        # For this demo, we'll simulate by checking transaction state
        await database_mock.connect()
        await database_mock.begin_transaction()
        
        assert database_mock.transaction_active == True
        
        # Simulate rollback
        await database_mock.rollback()
        assert database_mock.transaction_active == False
        
        await database_mock.disconnect()
    
    # Run integration tests
    summary = await runner.run_tests()
    return summary

# Run integration testing demo
asyncio.run(integration_testing_demo())

# =============================================================================
# 3. PERFORMANCE TESTING
# =============================================================================

print("\n=== Performance Testing ===")

@dataclass
class PerformanceMetrics:
    """Performance test metrics"""
    test_name: str
    total_requests: int
    successful_requests: int
    failed_requests: int
    total_duration: float
    min_response_time: float
    max_response_time: float
    avg_response_time: float
    median_response_time: float
    p95_response_time: float
    p99_response_time: float
    requests_per_second: float
    error_rate: float
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "test_name": self.test_name,
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "total_duration": self.total_duration,
            "min_response_time": self.min_response_time,
            "max_response_time": self.max_response_time,
            "avg_response_time": self.avg_response_time,
            "median_response_time": self.median_response_time,
            "p95_response_time": self.p95_response_time,
            "p99_response_time": self.p99_response_time,
            "requests_per_second": self.requests_per_second,
            "error_rate_percent": self.error_rate * 100
        }

class LoadTester:
    """Load testing framework"""
    
    def __init__(self):
        self.test_functions = {}
        self.results = []
    
    def register_test(self, name: str, test_function: Callable):
        """Register performance test function"""
        self.test_functions[name] = test_function
        print(f"⚡ Performance test registered: {name}")
    
    async def run_load_test(self, test_name: str, concurrent_users: int, 
                           duration_seconds: float, ramp_up_seconds: float = 0) -> PerformanceMetrics:
        """Run load test"""
        if test_name not in self.test_functions:
            raise ValueError(f"Test {test_name} not found")
        
        print(f"\n🚀 Starting load test: {test_name}")
        print(f"   Concurrent users: {concurrent_users}")
        print(f"   Duration: {duration_seconds}s")
        print(f"   Ramp-up: {ramp_up_seconds}s")
        
        test_function = self.test_functions[test_name]
        response_times = []
        errors = []
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        # Create semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(concurrent_users)
        
        async def worker():
            """Worker function to execute tests"""
            while time.time() < end_time:
                async with semaphore:
                    request_start = time.time()
                    try:
                        await test_function()
                        request_time = time.time() - request_start
                        response_times.append(request_time)
                    except Exception as e:
                        request_time = time.time() - request_start
                        response_times.append(request_time)
                        errors.append(str(e))
                    
                    # Small delay to prevent overwhelming
                    await asyncio.sleep(0.001)
        
        # Start workers
        tasks = []
        
        # Ramp up gradually if specified
        if ramp_up_seconds > 0:
            ramp_up_delay = ramp_up_seconds / concurrent_users
            for i in range(concurrent_users):
                await asyncio.sleep(ramp_up_delay)
                task = asyncio.create_task(worker())
                tasks.append(task)
        else:
            # Start all workers immediately
            for _ in range(concurrent_users):
                task = asyncio.create_task(worker())
                tasks.append(task)
        
        # Wait for test duration
        await asyncio.sleep(duration_seconds)
        
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*tasks, return_exceptions=True)
        
        total_duration = time.time() - start_time
        
        # Calculate metrics
        metrics = self._calculate_metrics(
            test_name, response_times, errors, total_duration
        )
        
        self.results.append(metrics)
        self._print_metrics(metrics)
        
        return metrics
    
    def _calculate_metrics(self, test_name: str, response_times: List[float], 
                          errors: List[str], total_duration: float) -> PerformanceMetrics:
        """Calculate performance metrics"""
        if not response_times:
            return PerformanceMetrics(
                test_name=test_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=len(errors),
                total_duration=total_duration,
                min_response_time=0,
                max_response_time=0,
                avg_response_time=0,
                median_response_time=0,
                p95_response_time=0,
                p99_response_time=0,
                requests_per_second=0,
                error_rate=1.0 if errors else 0
            )
        
        total_requests = len(response_times)
        successful_requests = total_requests - len(errors)
        failed_requests = len(errors)
        
        # Sort response times for percentile calculations
        sorted_times = sorted(response_times)
        
        min_time = min(response_times)
        max_time = max(response_times)
        avg_time = sum(response_times) / len(response_times)
        median_time = statistics.median(response_times)
        
        # Calculate percentiles
        def percentile(data: List[float], p: float) -> float:
            if not data:
                return 0
            k = (len(data) - 1) * p / 100
            f = int(k)
            c = k - f
            if f + 1 < len(data):
                return data[f] * (1 - c) + data[f + 1] * c
            else:
                return data[f]
        
        p95_time = percentile(sorted_times, 95)
        p99_time = percentile(sorted_times, 99)
        
        requests_per_second = total_requests / total_duration if total_duration > 0 else 0
        error_rate = len(errors) / total_requests if total_requests > 0 else 0
        
        return PerformanceMetrics(
            test_name=test_name,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
            total_duration=total_duration,
            min_response_time=min_time,
            max_response_time=max_time,
            avg_response_time=avg_time,
            median_response_time=median_time,
            p95_response_time=p95_time,
            p99_response_time=p99_time,
            requests_per_second=requests_per_second,
            error_rate=error_rate
        )
    
    def _print_metrics(self, metrics: PerformanceMetrics):
        """Print performance metrics"""
        print(f"\n📊 Performance Test Results: {metrics.test_name}")
        print(f"{'='*50}")
        print(f"Total Requests: {metrics.total_requests}")
        print(f"✅ Successful: {metrics.successful_requests}")
        print(f"❌ Failed: {metrics.failed_requests}")
        print(f"Error Rate: {metrics.error_rate*100:.2f}%")
        print(f"Duration: {metrics.total_duration:.2f}s")
        print(f"RPS: {metrics.requests_per_second:.2f}")
        print(f"\nResponse Times:")
        print(f"  Min: {metrics.min_response_time*1000:.2f}ms")
        print(f"  Max: {metrics.max_response_time*1000:.2f}ms")
        print(f"  Avg: {metrics.avg_response_time*1000:.2f}ms")
        print(f"  Median: {metrics.median_response_time*1000:.2f}ms")
        print(f"  95th percentile: {metrics.p95_response_time*1000:.2f}ms")
        print(f"  99th percentile: {metrics.p99_response_time*1000:.2f}ms")

class StressTester:
    """Stress testing framework"""
    
    def __init__(self, load_tester: LoadTester):
        self.load_tester = load_tester
    
    async def run_stress_test(self, test_name: str, max_users: int, 
                             step_duration: int = 30, step_size: int = 10) -> List[PerformanceMetrics]:
        """Run stress test by gradually increasing load"""
        print(f"\n🔥 Starting stress test: {test_name}")
        print(f"   Max users: {max_users}")
        print(f"   Step duration: {step_duration}s")
        print(f"   Step size: {step_size} users")
        
        results = []
        current_users = step_size
        
        while current_users <= max_users:
            print(f"\n📈 Testing with {current_users} concurrent users...")
            
            metrics = await self.load_tester.run_load_test(
                test_name, current_users, step_duration
            )
            
            results.append(metrics)
            
            # Check if system is degrading significantly
            if metrics.error_rate > 0.1:  # More than 10% errors
                print(f"⚠️ High error rate detected: {metrics.error_rate*100:.1f}%")
            
            if metrics.avg_response_time > 5.0:  # More than 5 seconds
                print(f"⚠️ High response time detected: {metrics.avg_response_time:.2f}s")
                print("🛑 System may be reaching its limits")
                break
            
            current_users += step_size
        
        self._print_stress_summary(results)
        return results
    
    def _print_stress_summary(self, results: List[PerformanceMetrics]):
        """Print stress test summary"""
        print(f"\n🏁 Stress Test Summary")
        print(f"{'='*60}")
        print(f"{'Users':<8} {'RPS':<8} {'Avg RT':<10} {'Error %':<8}")
        print(f"{'-'*35}")
        
        for metrics in results:
            # Estimate concurrent users from requests/duration
            users = int(metrics.total_requests / metrics.total_duration) if metrics.total_duration > 0 else 0
            print(f"{users:<8} {metrics.requests_per_second:<8.1f} {metrics.avg_response_time*1000:<10.1f} {metrics.error_rate*100:<8.1f}")

class BenchmarkTester:
    """Benchmark testing for comparing performance"""
    
    def __init__(self):
        self.benchmarks = {}
    
    async def benchmark(self, name: str, function: Callable, iterations: int = 1000) -> dict:
        """Benchmark a function"""
        print(f"\n🏃 Benchmarking: {name} ({iterations} iterations)")
        
        execution_times = []
        errors = 0
        
        start_time = time.time()
        
        for i in range(iterations):
            iter_start = time.time()
            
            try:
                if asyncio.iscoroutinefunction(function):
                    await function()
                else:
                    function()
                
                iter_time = time.time() - iter_start
                execution_times.append(iter_time)
                
            except Exception as e:
                errors += 1
                iter_time = time.time() - iter_start
                execution_times.append(iter_time)
        
        total_time = time.time() - start_time
        
        # Calculate statistics
        if execution_times:
            min_time = min(execution_times)
            max_time = max(execution_times)
            avg_time = sum(execution_times) / len(execution_times)
            median_time = statistics.median(execution_times)
        else:
            min_time = max_time = avg_time = median_time = 0
        
        result = {
            "name": name,
            "iterations": iterations,
            "total_time": total_time,
            "successful_iterations": iterations - errors,
            "errors": errors,
            "min_time": min_time,
            "max_time": max_time,
            "avg_time": avg_time,
            "median_time": median_time,
            "iterations_per_second": iterations / total_time if total_time > 0 else 0
        }
        
        self.benchmarks[name] = result
        self._print_benchmark_result(result)
        
        return result
    
    def _print_benchmark_result(self, result: dict):
        """Print benchmark result"""
        print(f"📈 Benchmark Results: {result['name']}")
        print(f"   Iterations: {result['iterations']}")
        print(f"   ✅ Successful: {result['successful_iterations']}")
        print(f"   ❌ Errors: {result['errors']}")
        print(f"   Total Time: {result['total_time']:.3f}s")
        print(f"   Avg Time: {result['avg_time']*1000:.3f}ms")
        print(f"   Min Time: {result['min_time']*1000:.3f}ms")
        print(f"   Max Time: {result['max_time']*1000:.3f}ms")
        print(f"   Iterations/sec: {result['iterations_per_second']:.2f}")
    
    def compare_benchmarks(self, baseline: str, *comparison_names):
        """Compare benchmarks against baseline"""
        if baseline not in self.benchmarks:
            print(f"❌ Baseline benchmark '{baseline}' not found")
            return
        
        baseline_result = self.benchmarks[baseline]
        baseline_avg = baseline_result['avg_time']
        
        print(f"\n📊 Benchmark Comparison (baseline: {baseline})")
        print(f"{'='*60}")
        print(f"{'Benchmark':<20} {'Avg Time':<12} {'vs Baseline':<15}")
        print(f"{'-'*50}")
        
        # Print baseline
        print(f"{baseline:<20} {baseline_avg*1000:<12.3f} {'100.0%':<15}")
        
        # Print comparisons
        for name in comparison_names:
            if name in self.benchmarks:
                result = self.benchmarks[name]
                avg_time = result['avg_time']
                
                if baseline_avg > 0:
                    ratio = (avg_time / baseline_avg) * 100
                    if ratio < 100:
                        performance = f"{100-ratio:.1f}% faster"
                    else:
                        performance = f"{ratio-100:.1f}% slower"
                else:
                    performance = "N/A"
                
                print(f"{name:<20} {avg_time*1000:<12.3f} {performance:<15}")

# Performance testing demonstration
print("Performance testing örnekleri:")

async def performance_testing_demo():
    # Setup test environment
    load_tester = LoadTester()
    stress_tester = StressTester(load_tester)
    benchmark_tester = BenchmarkTester()
    
    # Sample service for testing
    class TestService:
        def __init__(self):
            self.data = {}
            self.counter = 0
        
        async def fast_operation(self):
            """Fast operation for testing"""
            self.counter += 1
            await asyncio.sleep(0.001)  # 1ms
            return {"result": "success", "counter": self.counter}
        
        async def slow_operation(self):
            """Slow operation for testing"""
            self.counter += 1
            await asyncio.sleep(0.1)  # 100ms
            return {"result": "success", "counter": self.counter}
        
        async def unreliable_operation(self):
            """Unreliable operation that sometimes fails"""
            self.counter += 1
            await asyncio.sleep(random.uniform(0.01, 0.05))
            
            # 10% chance of failure
            if random.random() < 0.1:
                raise Exception("Random failure")
            
            return {"result": "success", "counter": self.counter}
        
        def cpu_intensive_sync(self):
            """CPU intensive synchronous operation"""
            result = 0
            for i in range(10000):
                result += i * i
            return result
        
        async def cpu_intensive_async(self):
            """CPU intensive asynchronous operation"""
            result = 0
            for i in range(10000):
                result += i * i
                if i % 1000 == 0:
                    await asyncio.sleep(0)  # Yield control
            return result
    
    service = TestService()
    
    # Register performance tests
    load_tester.register_test("fast_operation", service.fast_operation)
    load_tester.register_test("slow_operation", service.slow_operation)
    load_tester.register_test("unreliable_operation", service.unreliable_operation)
    
    # 1. Load Testing
    print("\n--- Load Testing ---")
    
    # Test fast operation
    await load_tester.run_load_test(
        "fast_operation", 
        concurrent_users=10, 
        duration_seconds=5
    )
    
    # Test slow operation
    await load_tester.run_load_test(
        "slow_operation",
        concurrent_users=5,
        duration_seconds=3
    )
    
    # Test unreliable operation
    await load_tester.run_load_test(
        "unreliable_operation",
        concurrent_users=8,
        duration_seconds=4
    )
    
    # 2. Stress Testing
    print("\n--- Stress Testing ---")
    
    stress_results = await stress_tester.run_stress_test(
        "fast_operation",
        max_users=50,
        step_duration=3,
        step_size=10
    )
    
    # 3. Benchmark Testing
    print("\n--- Benchmark Testing ---")
    
    # Benchmark CPU intensive operations
    await benchmark_tester.benchmark(
        "cpu_intensive_sync",
        service.cpu_intensive_sync,
        iterations=100
    )
    
    await benchmark_tester.benchmark(
        "cpu_intensive_async", 
        service.cpu_intensive_async,
        iterations=100
    )
    
    # Compare benchmarks
    benchmark_tester.compare_benchmarks(
        "cpu_intensive_sync",
        "cpu_intensive_async"
    )
    
    # 4. Memory Performance Test
    print("\n--- Memory Performance Test ---")
    
    async def memory_test():
        """Test memory allocation performance"""
        data = []
        for i in range(1000):
            data.append({"id": i, "data": f"test_data_{i}" * 10})
        return len(data)
    
    await benchmark_tester.benchmark("memory_allocation", memory_test, iterations=50)

# =============================================================================
# 4. TEST AUTOMATION & CI/CD
# =============================================================================

print("\n=== Test Automation & CI/CD ===")

class TestSuite:
    """Comprehensive test suite"""
    
    def __init__(self):
        self.unit_tests = []
        self.integration_tests = []
        self.performance_tests = []
        self.results = {}
    
    def add_unit_test(self, test_case: TestCase):
        """Add unit test"""
        self.unit_tests.append(test_case)
    
    def add_integration_test(self, name: str, test_function: Callable):
        """Add integration test"""
        self.integration_tests.append({
            "name": name,
            "function": test_function
        })
    
    def add_performance_test(self, name: str, test_function: Callable):
        """Add performance test"""
        self.performance_tests.append({
            "name": name,
            "function": test_function
        })
    
    async def run_full_suite(self, include_performance: bool = False) -> dict:
        """Run complete test suite"""
        print(f"\n🎯 Running Full Test Suite")
        print(f"{'='*60}")
        
        suite_start_time = time.time()
        
        # Run unit tests
        print("\n1️⃣ Running Unit Tests...")
        unit_runner = TestRunner()
        
        for test_case in self.unit_tests:
            unit_runner.add_test(test_case)
        
        unit_results = await unit_runner.run_tests()
        self.results["unit_tests"] = unit_results
        
        # Run integration tests
        print("\n2️⃣ Running Integration Tests...")
        integration_results = {"total": 0, "passed": 0, "failed": 0, "results": []}
        
        for test_info in self.integration_tests:
            start_time = time.time()
            
            try:
                if asyncio.iscoroutinefunction(test_info["function"]):
                    await test_info["function"]()
                else:
                    test_info["function"]()
                
                result = {
                    "name": test_info["name"],
                    "status": "PASSED",
                    "execution_time": time.time() - start_time
                }
                integration_results["passed"] += 1
                print(f"✅ {test_info['name']}")
                
            except Exception as e:
                result = {
                    "name": test_info["name"],
                    "status": "FAILED",
                    "execution_time": time.time() - start_time,
                    "error": str(e)
                }
                integration_results["failed"] += 1
                print(f"❌ {test_info['name']}: {str(e)}")
            
            integration_results["results"].append(result)
            integration_results["total"] += 1
        
        self.results["integration_tests"] = integration_results
        
        # Run performance tests if requested
        if include_performance:
            print("\n3️⃣ Running Performance Tests...")
            load_tester = LoadTester()
            performance_results = []
            
            for test_info in self.performance_tests:
                load_tester.register_test(test_info["name"], test_info["function"])
                metrics = await load_tester.run_load_test(
                    test_info["name"],
                    concurrent_users=5,
                    duration_seconds=2
                )
                performance_results.append(metrics.to_dict())
            
            self.results["performance_tests"] = {
                "total": len(performance_results),
                "results": performance_results
            }
        
        # Calculate overall results
        total_duration = time.time() - suite_start_time
        
        overall_results = {
            "suite_duration": total_duration,
            "unit_tests": self.results["unit_tests"],
            "integration_tests": self.results["integration_tests"]
        }
        
        if include_performance:
            overall_results["performance_tests"] = self.results["performance_tests"]
        
        self._print_suite_summary(overall_results)
        
        return overall_results
    
    def _print_suite_summary(self, results: dict):
        """Print test suite summary"""
        print(f"\n🏆 Test Suite Summary")
        print(f"{'='*60}")
        print(f"Total Duration: {results['suite_duration']:.2f}s")
        
        # Unit tests summary
        unit = results["unit_tests"]
        print(f"\n📝 Unit Tests:")
        print(f"   Total: {unit['total']}")
        print(f"   ✅ Passed: {unit['passed']}")
        print(f"   ❌ Failed: {unit['failed']}")
        print(f"   Success Rate: {unit['success_rate']:.1f}%")
        
        # Integration tests summary
        integration = results["integration_tests"]
        print(f"\n🔧 Integration Tests:")
        print(f"   Total: {integration['total']}")
        print(f"   ✅ Passed: {integration['passed']}")
        print(f"   ❌ Failed: {integration['failed']}")
        
        # Performance tests summary (if included)
        if "performance_tests" in results:
            perf = results["performance_tests"]
            print(f"\n⚡ Performance Tests:")
            print(f"   Total: {perf['total']}")
        
        # Overall pass/fail
        total_tests = unit['total'] + integration['total']
        total_passed = unit['passed'] + integration['passed']
        
        if total_tests > 0:
            overall_success_rate = (total_passed / total_tests) * 100
            print(f"\n🎯 Overall Success Rate: {overall_success_rate:.1f}%")
            
            if overall_success_rate == 100:
                print("🎉 All tests passed!")
            elif overall_success_rate >= 90:
                print("✅ Test suite mostly successful")
            else:
                print("⚠️ Test suite needs attention")

class CIPipeline:
    """Continuous Integration Pipeline"""
    
    def __init__(self):
        self.stages = []
        self.artifacts = {}
    
    def add_stage(self, name: str, stage_function: Callable):
        """Add pipeline stage"""
        self.stages.append({
            "name": name,
            "function": stage_function
        })
        print(f"🔧 Pipeline stage added: {name}")
    
    async def run_pipeline(self) -> dict:
        """Run CI/CD pipeline"""
        print(f"\n🚀 Starting CI/CD Pipeline")
        print(f"{'='*60}")
        
        pipeline_start_time = time.time()
        results = {"stages": [], "overall_status": "SUCCESS"}
        
        for i, stage in enumerate(self.stages, 1):
            stage_start_time = time.time()
            
            print(f"\n{i}️⃣ Stage: {stage['name']}")
            print(f"{'-'*40}")
            
            try:
                if asyncio.iscoroutinefunction(stage["function"]):
                    stage_result = await stage["function"]()
                else:
                    stage_result = stage["function"]()
                
                stage_duration = time.time() - stage_start_time
                
                stage_info = {
                    "name": stage["name"],
                    "status": "SUCCESS",
                    "duration": stage_duration,
                    "result": stage_result
                }
                
                print(f"✅ Stage '{stage['name']}' completed successfully ({stage_duration:.2f}s)")
                
            except Exception as e:
                stage_duration = time.time() - stage_start_time
                
                stage_info = {
                    "name": stage["name"],
                    "status": "FAILED",
                    "duration": stage_duration,
                    "error": str(e)
                }
                
                print(f"❌ Stage '{stage['name']}' failed: {str(e)}")
                results["overall_status"] = "FAILED"
                
                # Stop pipeline on failure
                results["stages"].append(stage_info)
                break
            
            results["stages"].append(stage_info)
        
        pipeline_duration = time.time() - pipeline_start_time
        results["total_duration"] = pipeline_duration
        
        self._print_pipeline_summary(results)
        
        return results
    
    def _print_pipeline_summary(self, results: dict):
        """Print pipeline summary"""
        print(f"\n🏁 Pipeline Summary")
        print(f"{'='*60}")
        print(f"Overall Status: {results['overall_status']}")
        print(f"Total Duration: {results['total_duration']:.2f}s")
        
        print(f"\nStage Results:")
        for stage in results["stages"]:
            status_icon = "✅" if stage["status"] == "SUCCESS" else "❌"
            print(f"{status_icon} {stage['name']}: {stage['status']} ({stage['duration']:.2f}s)")

# Test automation demonstration
print("Test automation & CI/CD örnekleri:")

async def test_automation_demo():
    # Create comprehensive test suite
    test_suite = TestSuite()
    
    # Sample application components
    calculator = Calculator()
    user_service = UserService()
    
    # Add unit tests
    def test_calc_basic_ops(assertions: TestAssertions):
        result = calculator.add(5, 3)
        assertions.assert_equal(result, 8)
        
        result = calculator.multiply(4, 3)
        assertions.assert_equal(result, 12)
    
    def test_user_creation(assertions: TestAssertions):
        user = user_service.create_user("test@example.com", "Test User")
        assertions.assert_not_none(user["id"])
        assertions.assert_equal(user["email"], "test@example.com")
    
    test_suite.add_unit_test(TestCase(
        name="test_calc_basic_ops",
        description="Test basic calculator operations",
        test_function=test_calc_basic_ops
    ))
    
    test_suite.add_unit_test(TestCase(
        name="test_user_creation",
        description="Test user creation",
        test_function=test_user_creation
    ))
    
    # Add integration tests
    async def integration_calc_user():
        """Integration test combining calculator and user service"""
        user = user_service.create_user("calc@example.com", "Calculator User")
        result = calculator.add(user["id"], 10)
        assert result > 10  # Should be user_id + 10
    
    test_suite.add_integration_test("integration_calc_user", integration_calc_user)
    
    # Add performance tests
    async def perf_test_calculation():
        for _ in range(100):
            calculator.add(random.randint(1, 100), random.randint(1, 100))
    
    test_suite.add_performance_test("perf_calculation", perf_test_calculation)
    
    # Run full test suite
    print("\n--- Running Full Test Suite ---")
    suite_results = await test_suite.run_full_suite(include_performance=True)
    
    # Setup CI/CD Pipeline
    print("\n--- CI/CD Pipeline ---")
    pipeline = CIPipeline()
    
    # Pipeline stages
    def stage_code_quality():
        """Code quality checks"""
        print("  🔍 Running linting...")
        print("  📏 Checking code style...")
        print("  🔒 Security scanning...")
        return {"linting": "passed", "style": "passed", "security": "passed"}
    
    async def stage_unit_tests():
        """Run unit tests"""
        print("  🧪 Executing unit tests...")
        # Reuse test runner
        runner = TestRunner()
        for test_case in test_suite.unit_tests:
            runner.add_test(test_case)
        
        results = await runner.run_tests()
        
        if results["failed"] > 0 or results["errors"] > 0:
            raise Exception(f"Unit tests failed: {results['failed']} failures, {results['errors']} errors")
        
        return {"tests_passed": results["passed"], "success_rate": results["success_rate"]}
    
    async def stage_integration_tests():
        """Run integration tests"""
        print("  🔗 Executing integration tests...")
        
        for test_info in test_suite.integration_tests:
            try:
                await test_info["function"]()
                print(f"    ✅ {test_info['name']}")
            except Exception as e:
                raise Exception(f"Integration test {test_info['name']} failed: {str(e)}")
        
        return {"integration_tests": "all_passed"}
    
    def stage_build_artifact():
        """Build deployment artifact"""
        print("  📦 Building application...")
        print("  🏗️ Creating deployment package...")
        
        artifact_info = {
            "version": "1.0.0",
            "build_time": datetime.utcnow().isoformat(),
            "commit_hash": "abc123def456"
        }
        
        return artifact_info
    
    def stage_deploy():
        """Deploy to staging"""
        print("  🚀 Deploying to staging environment...")
        print("  ✅ Deployment successful")
        
        return {"environment": "staging", "status": "deployed"}
    
    # Add stages to pipeline
    pipeline.add_stage("Code Quality", stage_code_quality)
    pipeline.add_stage("Unit Tests", stage_unit_tests)
    pipeline.add_stage("Integration Tests", stage_integration_tests)
    pipeline.add_stage("Build Artifact", stage_build_artifact)
    pipeline.add_stage("Deploy to Staging", stage_deploy)
    
    # Run pipeline
    pipeline_results = await pipeline.run_pipeline()
    
    # Pipeline results analysis
    if pipeline_results["overall_status"] == "SUCCESS":
        print("\n🎉 Pipeline completed successfully!")
        print("   Ready for production deployment")
    else:
        print("\n💥 Pipeline failed!")
        print("   Check logs and fix issues before retry")

# Run performance testing demo
asyncio.run(performance_testing_demo())

# Run test automation demo
asyncio.run(test_automation_demo())

print("\n" + "="*60)
print("TEST STRATEJİLERİ TAMAMLANDI")
print("="*60)

print("\nKonular Özeti:")
print("1. Unit Testing Framework (Custom Implementation)")
print("2. Test Assertions & Test Runner")
print("3. Integration Testing with Mocks")
print("4. Performance Testing (Load, Stress, Benchmark)")
print("5. Test Automation & CI/CD Pipelines")
print("6. Test Suite Organization")
print("7. Continuous Integration Stages")
print("8. Test Result Analysis & Reporting")

print("\nBir sonraki dosya: deployment_devops.py")