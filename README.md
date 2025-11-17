# Daily Weather and Road Risk Concierge Agent

Track: Concierge Agents  
Capstone for the Google 5 Day AI Agents Intensive (Nov 2025)

## 1. Problem

In mountain areas daily weather and road conditions can change quickly. To decide how to drive, I usually:

- Open a weather app or two  
- Look at temperature, precipitation and wind  
- Mentally translate that into "How risky are the roads today"  

This takes time and I can miss important details like strong winds on high bridges or very low temperatures that increase icing.

## 2. Solution

This project is a very small multi agent system that turns weather data into a daily road risk briefing.

You ask in natural language, for example:

> "What are the weather and road conditions for Silverthorne this morning"

The system:

1. Uses a **Coordinator Agent** to parse your question  
2. Calls a **Weather Agent** that uses a `get_weather` tool to get or simulate the forecast  
3. Calls a **Safety Agent** that interprets the forecast into road risk and driving tips  
4. Returns a concise summary

Example response:

> "Between 7 AM and noon you can expect light snow, temperatures around -6 C and wind gusts up to 20 mph. There is moderate risk of icy bridges. Drive more slowly, increase your following distance and avoid sudden braking on bridges."

## 3. Architecture

Agents:

- **Coordinator Agent**
  - Entry point for user queries
  - Orchestrates Weather Agent and Safety Agent
  - Combines their outputs into the final answer

- **Weather Agent**
  - Uses the `get_weather` tool
  - Currently returns a small simulated forecast object so this project stays simple
  - Can be easily swapped for a real weather API

- **Safety Agent**
  - Uses an LLM (Gemini) to turn weather into road risk
  - Produces:
    - a risk level: low, moderate, high
    - a short explanation and a few d
