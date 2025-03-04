import logging
import azure.functions as func
from .scraper import save_news_to_blob

app = func.FunctionApp()

@app.function_name(name="news_scraper")
@app.schedule(schedule="0 30 23 * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False)
def news_scraper(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.warning("The timer is past due!")

    logging.info("🔍 Running news scraper function...")
    save_news_to_blob()
    logging.info("✅ News scraper function completed.")
