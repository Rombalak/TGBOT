#!/bin/bash
source venv/bin/activate
nohup python src/bot.py > logs/bot.log 2>&1 &
echo "Bot started in background"
