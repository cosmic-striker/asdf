#!/usr/bin/env python3
"""
Admin User Management Script for ExploitX
Usage: python manage_admin.py [create|reset|list]
"""

import sys
import os
from werkzeug.security import generate_password_hash

# Add the exploitx directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'exploitx'))

from exploitx.app import app, db, User

def create_admin(username='admin', password='admin123', is_super_admin=True):
    """Create an admin user"""
    with app.app_context():
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"User '{username}' already exists!")
            return False
        
        # Create new admin user
        admin = User(
            username=username,
            is_admin=True,
            is_super_admin=is_super_admin
        )
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        
        print(f"Admin user '{username}' created successfully!")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Super Admin: {is_super_admin}")
        return True

def reset_admin_password(username='admin', new_password='admin123'):
    """Reset admin user password"""
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if not user:
            print(f"User '{username}' not found!")
            return False
        
        user.set_password(new_password)
        db.session.commit()
        
        print(f"Password for user '{username}' reset successfully!")
        print(f"New password: {new_password}")
        return True

def list_users():
    """List all users"""
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found!")
            return
        
        print("Users:")
        print("-" * 50)
        for user in users:
            admin_type = "Super Admin" if user.is_super_admin else "Admin" if user.is_admin else "User"
            print(f"ID: {user.id}")
            print(f"Username: {user.username}")
            print(f"Type: {admin_type}")
            print(f"Created: {user.created_at}")
            print(f"Last Login: {user.last_login or 'Never'}")
            print("-" * 50)

def main():
    if len(sys.argv) < 2:
        print("Usage: python manage_admin.py [create|reset|list]")
        print("Commands:")
        print("  create [username] [password] - Create admin user")
        print("  reset [username] [password]  - Reset admin password")
        print("  list                        - List all users")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'create':
        username = sys.argv[2] if len(sys.argv) > 2 else 'admin'
        password = sys.argv[3] if len(sys.argv) > 3 else 'admin123'
        create_admin(username, password)
    
    elif command == 'reset':
        username = sys.argv[2] if len(sys.argv) > 2 else 'admin'
        password = sys.argv[3] if len(sys.argv) > 3 else 'admin123'
        reset_admin_password(username, password)
    
    elif command == 'list':
        list_users()
    
    else:
        print(f"Unknown command: {command}")
        print("Available commands: create, reset, list")

if __name__ == '__main__':
    main() 