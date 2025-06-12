#!/usr/bin/env python3
"""
Startup script for CV Optimizer Pro on Render
Ensures proper database initialization and environment setup
"""

import os
import sys
import logging
from app import app, db, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_production():
    """Initialize the application for production deployment"""
    try:
        with app.app_context():
            # Create all database tables
            db.create_all()
            logger.info("Database tables created successfully")
            
            # Create developer account if it doesn't exist
            dev_user = User.query.filter_by(username='developer').first()
            if not dev_user:
                dev_user = User(
                    username='developer',
                    email='dev@cvoptimizer.pro',
                    first_name='Developer',
                    last_name='Admin'
                )
                dev_user.set_password('DevAdmin2024!')
                db.session.add(dev_user)
                db.session.commit()
                logger.info("Developer account created successfully")
            else:
                logger.info("Developer account already exists")
                
            # Verify required environment variables
            required_vars = ['OPENROUTER_API_KEY', 'STRIPE_SECRET_KEY', 'VITE_STRIPE_PUBLIC_KEY']
            missing_vars = [var for var in required_vars if not os.environ.get(var)]
            
            if missing_vars:
                logger.warning(f"Missing environment variables: {', '.join(missing_vars)}")
                logger.warning("Some features may not work properly")
            else:
                logger.info("All required environment variables are set")
                
            logger.info("Production initialization completed successfully")
            return True
            
    except Exception as e:
        logger.error(f"Error during production initialization: {str(e)}")
        return False

if __name__ == '__main__':
    if initialize_production():
        logger.info("Application ready for production deployment")
        sys.exit(0)
    else:
        logger.error("Failed to initialize application")
        sys.exit(1)
