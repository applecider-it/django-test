from django.shortcuts import render, redirect
from django.utils import timezone
import json
import logging
from datetime import datetime

def home_view(request):
    return render(request, "home.html")

def development_view(request):
    logger = logging.getLogger(__name__)

    dt_now = datetime.now()
    tz_now = timezone.now()
    #dt_local_time = timezone.localtime(dt_now)
    tz_local_time = timezone.localtime(tz_now)

    logger.debug("デバッグメッセージ")
    logger.info("情報")
    logger.warning("警告")
    logger.error("エラー")
    logger.info(f"dt_now: {dt_now}")
    #logger.info(f"dt_local_time: {dt_local_time}")
    logger.info(f"tz_now: {tz_now}")
    logger.info(f"tz_local_time: {tz_local_time}")

    data = {"val1": "テスト"}
    return render(request, "development.html", {
        "data_json": json.dumps(data),
    })
