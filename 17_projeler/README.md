# Section 17 - Projeler (Real-World Applications)

Bu bölümde Python ile gerçek dünya projeleri geliştirmeyi öğreneceksiniz. Büyük ölçekli uygulamalar, API'lar, mikroservisler ve profesyonel proje yapıları ele alınacaktır.

## 📚 Bu Bölümde Öğrenecekleriniz

### 1. Proje Mimarisi ve Yapısı
- **Büyük proje organizasyonu**: Modüler yapı, package organizasyonu
- **Design patterns uygulama**: MVC, Repository, Service Layer patterns
- **Dependency injection**: IoC container, service registration
- **Configuration management**: Environment variables, config files
- **Logging ve monitoring**: Structured logging, metrics collection

### 2. RESTful API Geliştirme
- **FastAPI framework**: Modern API development
- **Authentication/Authorization**: JWT, OAuth2, RBAC
- **Database integration**: SQLAlchemy ORM, migrations
- **Input validation**: Pydantic models, request/response schemas
- **API documentation**: OpenAPI, Swagger UI
- **Error handling**: Custom exceptions, status codes

### 3. Mikroservis Mimarisi
- **Service decomposition**: Domain-driven design
- **Inter-service communication**: HTTP, message queues
- **Service discovery**: Health checks, load balancing
- **Data consistency**: Eventual consistency, saga pattern
- **Monitoring ve tracing**: Distributed tracing

### 4. Veritabanı İşlemleri
- **ORM ve Raw SQL**: SQLAlchemy advanced usage
- **Database migrations**: Alembic integration
- **Connection pooling**: Performance optimization
- **Caching strategies**: Redis, in-memory caching
- **Transaction management**: ACID properties

### 5. Test Stratejileri
- **Unit testing**: pytest, mock objects
- **Integration testing**: Database, API testing
- **Performance testing**: Load testing, profiling
- **Test coverage**: Coverage reports, quality metrics
- **CI/CD integration**: Automated testing pipelines

### 6. Deployment ve DevOps
- **Containerization**: Docker, docker-compose
- **Environment management**: Development, staging, production
- **Secrets management**: Environment variables, vault
- **Monitoring**: Application metrics, alerting
- **Scaling strategies**: Horizontal vs vertical scaling

## 🗂️ Dosya Yapısı

```
17_projeler/
├── README.md                          # Bu dosya
├── proje_mimarisi.py                 # Büyük proje yapısı ve patterns
├── restful_api_gelistirme.py         # FastAPI ile API development
├── mikroservis_mimarisi.py           # Mikroservis patterns ve communication
├── veritabani_islemleri.py           # Advanced database operations
├── test_stratejileri.py              # Comprehensive testing approaches
└── deployment_devops.py              # Deployment ve monitoring
```

## 🎯 Öğrenme Hedefleri

Bu bölümü tamamladığınızda:

- ✅ Büyük ölçekli Python projelerini organize edebileceksiniz
- ✅ Professional RESTful API'lar geliştirebileceksiniz
- ✅ Mikroservis mimarisini uygulayabileceksiniz
- ✅ Advanced veritabanı işlemlerini gerçekleştirebileceksiniz
- ✅ Kapsamlı test stratejileri geliştirebileceksiniz
- ✅ Production-ready deployment yapabileceksiniz

## 🚀 Pratik Projeler

Her dosyada aşağıdaki pratik projeler yer almaktadır:

1. **E-commerce Backend API**: Tam özellikli e-ticaret sistemi
2. **Task Management System**: Proje yönetim uygulaması
3. **Social Media Platform**: Sosyal medya backend
4. **Financial Trading System**: Trading bot ve portfolio management
5. **IoT Data Processing**: Sensor data processing pipeline
6. **Multi-tenant SaaS**: Çok kiracılı SaaS uygulaması

## 📋 Önkoşullar

Bu bölüme başlamadan önce aşağıdaki konularda bilgi sahibi olmanız önerilir:

- ✅ Python temelleri (Sections 1-10)
- ✅ Nesne yönelimli programlama (Section 16)
- ✅ Temel web development kavramları
- ✅ SQL ve veritabanı temelleri
- ✅ HTTP protocol basics

## 🔧 Gerekli Kütüphaneler

Bu bölümde kullanılacak ana kütüphaneler:

```bash
# API Development
pip install fastapi uvicorn

# Database
pip install sqlalchemy alembic psycopg2-binary

# Validation
pip install pydantic email-validator

# Authentication
pip install python-jose python-multipart passlib[bcrypt]

# Testing
pip install pytest pytest-asyncio httpx

# Utilities
pip install python-dotenv redis celery

# Monitoring
pip install prometheus-client structlog
```

## 🎓 Best Practices

Bu bölümde öğrenilecek best practices:

- **Clean Architecture**: Separation of concerns
- **SOLID Principles**: Maintainable code structure  
- **Security First**: Input validation, authentication
- **Performance**: Caching, query optimization
- **Monitoring**: Logging, metrics, tracing
- **Documentation**: API docs, code comments

## 📖 Ek Kaynaklar

- FastAPI Official Documentation
- SQLAlchemy Documentation
- pytest Documentation
- Docker Best Practices
- 12-Factor App Methodology
- RESTful API Design Guidelines

---

**Not**: Bu projeler production-ready kalitede yazılmıştır ve gerçek projelerde template olarak kullanılabilir.

**Sonraki Bölüm**: [Section 18 - Veri Analizi](../18_veri_analizi/README.md)