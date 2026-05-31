# AI-Powered Travel Planner

## Overview

Planning travel trips can often be time-consuming and overwhelming due to the need to gather information from multiple sources. This project aims to simplify the process by providing a Generative AI-powered travel planning assistant built using Google's Agent Development Kit (ADK).

The Travel Planner generates personalized travel recommendations, destination ideas, itinerary suggestions, and real-time travel insights by leveraging a multi-agent architecture.

---

## Features

### Personalized Travel Planning

* Generates travel recommendations based on user preferences.
* Suggests attractions, activities and hotels.
* Creates structured day-wise itineraries when requested.

### Travel Inspiration

* Recommends destinations and activities aligned with the user's interests.
* Provides travel tips.

### Real-Time Travel Information

* Retrieves current information using Google Search through a specialized News Agent.
* Supports:

  * Current events
  * Local safety updates
  * Travel advisories
  * Ongoing festivals and public events
  * Transport disruptions
  * Live schedules

---

## Architecture

```text
Travel Planner (Root Agent)
           |
           |
           v
Travel Inspiration Agent
      /            \
     /              \
    v                v
News Agent      Places Tool
(Agent Tool)   (Function Tool - WIP)
```

### 1. Travel Planner (Root Agent)

The root agent serves as the primary entry point for all user interactions.

Responsibilities:

* Understand user requests
* Manage workflow orchestration
* Ensure only travel-related requests are processed

The root agent does not generate detailed itineraries itself.

---

### 2. Travel Inspiration Agent

The Travel Inspiration Agent acts as the main reasoning and planning engine of the system.

Responsibilities:

* Generate personalized recommendations
* Create itineraries when requested
* Suggest attractions and activities
* Recommend local foods
* Decide when specialized tools should be invoked

The agent uses:

* Internal travel knowledge
* News Agent for real-time information
* Places Tool for location-based searches (currently under development)

---

### 3. News Agent (Agent-as-a-Tool)

The News Agent is implemented as an Agent Tool inside ADK.

Responsibilities:

* Retrieve real-time travel information
* Perform Google Search when current information is required

Examples:

* Current protests in Paris
* Ongoing festivals in Tokyo
* Travel advisories
* Local safety updates
* Current events affecting travel

The News Agent is only invoked when real-time information is required and is not used for normal itinerary generation.

---

### 4. Places Tool (Function Tool)

Current Status: Work in Progress

The Places Tool is being developed as a Function Tool using:

* Geopy
* OpenStreetMap (Nominatim)
* Overpass API

Planned Capabilities:

* Find nearby hotels
* Find nearby cafes
* Find nearby restaurants
* Find nearby attractions
* Retrieve geographic locations

Example Queries:

* Cafes near Eiffel Tower
* Hotels near Taj Mahal
* Restaurants near Times Square

---

## Project Structure

```text
PROJECT-1
│
├── travel_planner
│   ├── __init__.py
│   ├── agent.py
│   │
│   └── sub_agents
│       └── travel_inspiration_agent
│           ├── __init__.py
│           ├── agent.py
│           │
│           └── tools
│               ├── agent_tools
│               │     ├── __init__.py
│               │     └── agent.py
│               │
│               └── function_tools
│                   └── places_agent
│                       ├── __init__.py
│                       └── places_tool.py
│
├── requirements.txt
└── README.md
```

---

## Technology Stack

* Python
* Google ADK
* Gemini 2.5 Flash
* Google Search Tool
* Geopy
* OpenStreetMap
* Overpass API

---

## Current Progress

### Completed

* Root Agent implementation
* Travel Inspiration Agent implementation
* News Agent implementation
* Real-time information retrieval using Google Search

### In Progress

* Places Tool development
* Location-based search functionality
* Nearby amenities retrieval

---

## Example Queries

### Trip Planning

* Plan a 5-day trip to Paris
* Suggest a trip to Japan

### Real-Time Information

* Are there any protests in Paris right now?
* What festivals are happening in Tokyo this week?
* Are there any travel advisories for Bali?

### Location-Based Search (Upcoming)

* Cafes near Eiffel Tower
* Hotels near Taj Mahal
* Restaurants near Times Square

---

## Additional details

This project is intended for learning and experimentation with multi-agent AI systems using Google ADK.

---

## Running the Project Locally

Follow the steps below to run the Travel Planner application on your local machine.

### 1. Clone the Repository

```bash
git clone <repository-url>
```
Replace `<repository-url>` with the GitHub repository URL.

---

### 2. Open the Project in VS Code

Navigate to the folder where the repository was cloned.

Right-click the project folder and select:

```text
Open with Code
```

---

### 3. Verify Project Structure

Open a terminal in VS Code and run:

```bash
ls
```

You should see the following files and folders:

```text
travel_planner
.gitignore
README.md
requirements.txt
```

If these files are not visible:

* Verify that you are in the correct project directory.
* Check the current path.
* Navigate to the project root folder again.
* Re-run:

```bash
ls
```

until the above structure is visible.

---

### 4. Configure Environment Variables

Look into the `travel_planner` folder:

Locate the sample environment file:

```text
.env.sample
```

In the same level as .evn.sample file, Create a new file named:

```text
.env
```

Copy the contents from `.env.sample` and add your Google API key.

Example:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

### 5. Generate a Google API Key

To create a Google API key:

1. Open Google AI Studio.
2. Navigate to:

   ```text
   Google AI Studio → API Keys
   ```
3. Create a new API key.
4. Copy the generated key.
5. Paste it into the `.env` file.

---

### 6. Install Dependencies

From the project root directory, run:

```bash
pip install -r requirements.txt
```

This will install all required Python packages.

---

### 7. Start the ADK Web Interface

Run:

```bash
adk web
```

After the application starts successfully, a localhost URL will be displayed in the terminal.

Example:

```text
http://localhost:8000
```

---

### 8. Open the Application

Copy the localhost URL and paste it into your browser.

The ADK web interface should now be available.

---

### 9. Test the Application

Try some sample queries:

#### Trip Planning

```text
Plan a 5-day trip to Paris
```

#### Real-Time Information

```text
Are there any protests in Paris right now?
```

```text
What festivals are happening in Tokyo this week?
```

```text
Are there any travel advisories for Bali?
```

---

### Troubleshooting

#### Dependencies Not Installing

Ensure Python and pip are installed:

```bash
python --version
pip --version
```

---

#### API Key Issues

Verify that:

* `.env` exists inside the `travel_planner` directory.
* The API key is correctly copied.
* No extra spaces or quotation marks are present.

---

### Expected Workflow

```text
User
  ↓
Travel Planner (Root Agent)
  ↓
Travel Inspiration Agent
  ↓
News Agent (when real-time information is required)
```

The Places Tool integration is currently under development and will be available in future updates.

