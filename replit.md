# Overview

This repository contains a comprehensive Highrise bot system built in Python. It's a feature-rich Discord-style bot for the Highrise virtual world platform that provides advanced user management, moderation tools, emote systems, AI chat capabilities, and room management features. The bot is designed to serve Arabic-speaking communities with extensive moderation capabilities, custom commands, VIP systems, and automated features.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Core Bot Architecture
The system follows a modular architecture pattern with a central bot controller (`main.py`) and specialized modules for different functionalities. The main bot inherits from Highrise's `BaseBot` class and coordinates between various managers and handlers.

**Key Components:**
- **Main Bot Controller** (`main.py`): Central event handler and coordinator
- **Web Server** (`run.py`): Flask-based web interface for remote management
- **Modular System** (`modules/`): Specialized managers for different bot functions
- **Configuration Management** (`config.py`): Centralized configuration with security settings

## User Management System
Implements a hierarchical permission system with multiple user types and roles.

**Architecture Decisions:**
- **Unified User Checker**: Centralized permission validation across all systems
- **Historical Tracking**: Separate storage for active users vs. historical visitor data
- **Role-Based Access Control**: Hierarchical permissions (Owner > Admin > Moderator > VIP > User)
- **Real-time Synchronization**: Integration with Highrise's native permission system

## Command Processing Architecture
Uses a command handler pattern with permission-based routing and response management.

**Design Pattern:**
- **Central Command Router**: Routes commands based on user permissions
- **Modular Command Handlers**: Separate handlers for user, moderator, and VIP commands
- **Permission Validation**: Pre-execution permission checks
- **Response Management**: Unified response system with whisper/chat routing

## AI Integration System
Integrates Google Gemini AI for intelligent chat responses and code assistance.

**Technical Approach:**
- **Conversation Memory**: Persistent conversation history with context awareness
- **Advanced Analytics**: Message sentiment analysis and topic tracking
- **Code Generation**: AI-powered command creation and bug fixing capabilities
- **Personality System**: Configurable AI personality with learning capabilities

## Data Storage Strategy
Uses JSON-based file storage with modular data management for different system components.

**Storage Architecture:**
- **Modular Data Files**: Separate JSON files for different data types
- **Real-time Persistence**: Immediate save operations for critical data
- **Backup System**: Automated backup creation for updates
- **Data Integrity**: File validation and corruption recovery

## Emote and Animation System
Implements a sophisticated emote management system with timing controls and auto-dance features.

**Design Decisions:**
- **Timing Management**: Precise emote duration tracking
- **Auto-Dance System**: Idle user detection with automatic emote sequences
- **Custom Commands**: User-defined emote combinations
- **Performance Optimization**: Efficient emote queuing and execution

## Web Interface Architecture
Flask-based web server providing remote bot management capabilities.

**Interface Design:**
- **RESTful API**: JSON-based API endpoints for bot control
- **Real-time Updates**: Live status monitoring and control
- **Responsive UI**: Bootstrap-based responsive design
- **Security Features**: Permission-based access controls

# External Dependencies

## Core Framework Dependencies
- **Highrise Python SDK**: Primary bot framework for Highrise platform integration
- **AsyncIO**: Asynchronous programming support for concurrent operations
- **Flask**: Web server framework for management interface

## AI and Machine Learning
- **Google Gemini AI**: Advanced AI chat capabilities and code generation
- **Python-dotenv**: Environment variable management for API keys

## Web Interface Technologies
- **Bootstrap 5**: Frontend CSS framework for responsive UI
- **Font Awesome**: Icon library for UI elements
- **Prism.js**: Code syntax highlighting for AI assistant interface

## Data Management
- **JSON**: Primary data storage format for configuration and user data
- **Python AST**: Abstract syntax tree parsing for dynamic command loading

## Development and Utilities
- **Importlib**: Dynamic module loading for extensible command system
- **Zipfile/Shutil**: File management for update system and backups
- **Datetime**: Time-based operations for scheduling and logging

## Platform Integration
- **Highrise WebAPI**: Extended API access for room management features
- **Aiohttp**: HTTP client for external API communications

The system is designed to be self-contained with minimal external service dependencies, using file-based storage instead of external databases for simplicity and portability.