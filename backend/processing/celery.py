from celery import Celery

app = Celery('processing',
             broker='redis://localhost:6379/0',  # Use Redis as the message broker
             backend='redis://localhost:6379/0',  # Use Redis to store task results (optional)
             include=['backend.processing.tasks'])  # Import tasks from this module

# Optional configuration
app.conf.update(
    result_expires=3600,  # Results expire after 1 hour
)

if __name__ == '__main__':
    app.start()
