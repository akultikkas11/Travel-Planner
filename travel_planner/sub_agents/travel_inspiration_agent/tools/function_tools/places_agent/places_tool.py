from geopy.geocoders import Nominatim
import requests


def places_tool(
    query: str,
    loc: str,
    radius: int = 1500
    ) -> str:
    """
    Search for nearby places and amenities around a specified location.

    This tool is useful for finding nearby:
    - cafes
    - hotels
    - restaurants
    - tourist attractions
    - amenities

    The tool uses OpenStreetMap and Geopy services to:
    1. Convert a location name into geographic coordinates
    2. Search nearby places within a fixed radius

    Use this tool whenever the user asks for:
    - hotels near a landmark
    - cafes near a tourist attraction
    - restaurants near a location
    - nearby amenities
    - location-based recommendations

    Examples:
    - "cafes near Eiffel Tower"
    - "hotels near Taj Mahal"
    - "restaurants near Times Square"
    - "places to eat near Colosseum"

    Examples of query parsing:
    - User: "cafes near Eiffel Tower"
        -> places_tool(query="cafes", loc="Eiffel Tower")

    - User: "hotels near Taj Mahal"
        -> places_tool(query="hotels", loc="Taj Mahal")

    - User: "restaurants around Times Square"
        -> places_tool(query="restaurants", loc="Times Square")

    - User: "places to eat near Colosseum"
        -> places_tool(query="restaurants", loc="Colosseum")

    Args:
        query (str):
            Amenity or place category to search for.

            Examples:
            - cafes
            - restaurants
            - hotels
            - bars
            - parks

        loc (str):
            Landmark, attraction, city, or location name.

            Examples:
            - Eiffel Tower
            - Taj Mahal
            - Times Square
            - Colosseum

        radius (int, optional):
            Search radius in meters.

            Default:
            - 1500

    Returns:
        str:
            A formatted list of nearby places including:
            - place name
            - category/type

            Returns an error message if:
            - the location cannot be found
            - no nearby places are available
            - API lookup fails
            - geocoding fails
    """

    geolocator = Nominatim(
        user_agent="travel_planner",
        timeout=10
    )

    try:
        location = geolocator.geocode(loc)

        if not location:
            return f"Could not find the location: {loc}"

        lat = location.latitude
        lon = location.longitude

        print(f"Location received: {loc}")
        print(f"Query received: {query}")
        print("="*30)
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        print("="*30)

        # ---------------------------------------------------
        # Step 2: Map user query to OSM filters
        # ---------------------------------------------------
        query_mapping = {
            "cafes": '[amenity="cafe"]',
            "cafe": '[amenity="cafe"]',

            "restaurants": '[amenity="restaurant"]',
            "restaurant": '[amenity="restaurant"]',

            "hotels": '[tourism="hotel"]',
            "hotel": '[tourism="hotel"]',

            "bars": '[amenity="bar"]',
            "bar": '[amenity="bar"]',

            "parks": '[leisure="park"]',
            "park": '[leisure="park"]',

            "shops": '[shop]',
            "shop": '[shop]'
        }

        osm_filter = query_mapping.get(
            query.lower(),
            f'["name"~"{query}",i]'
        )

        # ---------------------------------------------------
        # Step 3: Build Overpass query
        # ---------------------------------------------------
        overpass_url = "https://overpass-api.de/api/interpreter"

        overpass_query = f"""
        [out:json];
        (
          node{osm_filter}(around:{radius},{lat},{lon});
          way{osm_filter}(around:{radius},{lat},{lon});
          relation{osm_filter}(around:{radius},{lat},{lon});
        );
        out center;
        """
        # ---------------------------------------------------
        # Step 4: Send API request
        # ---------------------------------------------------
        response = requests.get(
            overpass_url,
            params={"data": overpass_query},
            timeout=30
        )
        print(f"=========== response ===============")
        print(f"STATUS CODE: {response.status_code}")
        print(response.text[:500])
        print(f"====================================")

        if response.status_code != 200:
            return (
                f"Overpass API request failed "
                f"with status code {response.status_code}"
            )

        data = response.json()

        # ---------------------------------------------------
        # Step 5: Validate results
        # ---------------------------------------------------
        if not data.get("elements"):
            return f"No nearby places found near {query}"

        # ---------------------------------------------------
        # Step 6: Process results
        # ---------------------------------------------------
        results = []

        for place in data["elements"][:10]:

            tags = place.get("tags", {})

            name = tags.get("name", "Unnamed Place")

            # category = (
            #     tags.get("amenity")
            #     or tags.get("tourism")
            #     or "place"
            # )

            category = (
                tags.get("amenity")
                or tags.get("tourism")
                or tags.get("shop")
                or tags.get("leisure")
                or "place"
            )


            results.append(
                f"- {name} ({category})"
            )

        # ---------------------------------------------------
        # Step 7: Final formatted output
        # ---------------------------------------------------

        # final_result = f"Nearby {query} near {loc} around {radius} km:\n\n"
        # final_result += "\n".join(results)

        final_result = (
            f"Nearby {query} near {loc} "
            f"within {radius} meters:\n\n"
        )

        final_result += "\n".join(results)

        print("=" * 50)
        print(final_result)
        print("=" * 50)

        return final_result

    except Exception as e:
        print("="*50)
        print("ERROR OCCURRED")
        print(str(e))
        print("="*50)

        return f"Error finding places: {str(e)}"