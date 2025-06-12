
#!/usr/bin/env python3
"""
Production startup script for CV Optimizer Pro
Initializes database and creates necessary accounts
"""

import os
import sys
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def initialize_production():
    """Initialize the application for production deployment"""
    try:
        # Import app components after setting up logging
        from app import app, db, User
        
        logger.info("Starting production initialization...")
        
        with app.app_context():
            # Create all database tables
            db.create_all()
            logger.info("✅ Database tables created successfully")
            
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
                dev_user.has_paid = True  # Free access for developer
                dev_user.is_premium = True
                db.session.add(dev_user)
                db.session.commit()
                logger.info("✅ Developer account created successfully")
            else:
                # Ensure developer has premium access
                if not dev_user.has_paid:
                    dev_user.has_paid = True
                    dev_user.is_premium = True
                    db.session.commit()
                logger.info("✅ Developer account verified")
                
            # Verify required environment variables
            required_vars = ['OPENROUTER_API_KEY', 'STRIPE_SECRET_KEY', 'VITE_STRIPE_PUBLIC_KEY']
            missing_vars = [var for var in required_vars if not os.environ.get(var)]
            
            if missing_vars:
                logger.warning(f"⚠️  Missing environment variables: {', '.join(missing_vars)}")
                logger.warning("Some features may not work properly")
            else:
                logger.info("✅ All required environment variables are set")
            
            # Test database connection
            try:
                db.session.execute('SELECT 1')
                logger.info("✅ Database connection successful")
            except Exception as e:
                logger.error(f"❌ Database connection failed: {str(e)}")
                return False
                
            # Verify OpenRouter API key format
            api_key = os.environ.get('OPENROUTER_API_KEY', '')
            if api_key and api_key.startswith('sk-or-v1-'):
                logger.info("✅ OpenRouter API key format is valid")
            else:
                logger.warning("⚠️  OpenRouter API key format may be invalid")
                
            logger.info("🚀 Production initialization completed successfully")
            logger.info(f"🕒 Startup completed at: {datetime.now()}")
            return True
            
    except ImportError as e:
        logger.error(f"❌ Import error during initialization: {str(e)}")
        logger.error("Make sure all dependencies are installed")
        return False
    except Exception as e:
        logger.error(f"❌ Error during production initialization: {str(e)}")
        logger.error("Check your configuration and try again")
        return False

if __name__ == '__main__':
    logger.info("🎯 CV Optimizer Pro - Production Startup")
    logger.info("=" * 50)
    
    if initialize_production():
        logger.info("✅ Application ready for production deployment")
        logger.info("=" * 50)
        sys.exit(0)
    else:
        logger.error("❌ Failed to initialize application")
        logger.error("=" * 50)
        sys.exit(1)
