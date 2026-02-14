# main.py
# Social Media Manager Agent2 - Python Backend Demo
# Includes: Caption Generation + Image Input + Scheduling

import datetime


def generate_caption(topic):
    """
    Generate AI-like caption based on topic
    """
    return f"Boost your {topic} post! 🚀 #AI #SocialMedia #Marketing"


def schedule_post(caption, image_path):
    """
    Schedule post for tomorrow (Demo)
    """
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    time = f"{tomorrow} at 10:00 AM"

    print("\n--- Post Scheduled Successfully ---")
    print("Caption :", caption)
    print("Image   :", image_path)
    print("Time    :", time)
    print("----------------------------------")


def main():
    print("Welcome to Social Media Manager Agent (Python)\n")

    # User Inputs
    topic = input("Enter post topic: ")
    image_path = input("Enter image file path: ")

    # Generate Caption
    caption = generate_caption(topic)

    print("\nGenerated Caption:")
    print(caption)

    print("\nSelected Image:")
    print(image_path)

    # Schedule Post
    schedule_post(caption, image_path)


if __name__ == "__main__":
    main()
