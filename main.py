import cv2
import streamlit as st
import pandas as pd
from deepface import DeepFace
from urllib.parse import quote
import time
import os

path = r'C:\Users\KKP\mini_project'
os.chdir(path)

# Load the CSV files containing song information for each mood category
happy_songs_spotify_df = pd.read_csv('happy.csv')
happy_songs_names_df = pd.read_csv('happy1.csv')

sad_songs_spotify_df = pd.read_csv('sad.csv')
sad_songs_names_df = pd.read_csv('sad (2).csv')

angry_songs_spotify_df = pd.read_csv('calm.csv')
angry_songs_names_df = pd.read_csv('calm (2).csv')

romantic_songs_spotify_df = pd.read_csv('romantic.csv')
romantic_songs_names_df = pd.read_csv('romantic (2).csv')

fear_songs_spotify_df = pd.read_csv('fear.csv')
fear_songs_names_df = pd.read_csv('fear (2).csv')


def detect_emotion(frame):
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    dominant_mood = None

    if result and 'dominant_emotion' in result[0]:
        dominant_emotion = result[0]['dominant_emotion']

        mood_mapping = {
            'angry': 'angry',
            'sad': 'sad',
            'neutral': 'neutral',
            'happy': 'happy',
            'surprised': 'surprised',
            'disgusted': 'disgusted',
            'fearful': 'fear'
        }

        dominant_mood = mood_mapping.get(dominant_emotion, 'unknown')

    return dominant_mood


def main():
    st.title("Emotion-Based Song Recommendation")
    # Open webcam
    cap = cv2.VideoCapture(0)
    capture_duration = 5
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Cannot open webcam")
        return

    start_time = time.time()  # Track start time for capture duration
    dominant_mood = None
    detected_frame = None
    while True:
        # Read frame from webcam
        ret, frame = cap.read()

        # Check if frame is successfully read
        if not ret:
            print("Error: Cannot read frame")
            break

        # Perform emotion analysis on the frame
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Check if emotions are detected and a face is found
        if result and 'dominant_emotion' in result[0]:
            dominant_emotion = result[0]['dominant_emotion']

            # Map detected emotion to a mood category (enhancement)
            mood_mapping = {
                'angry': 'angry',
                'sad': 'sad',
                'neutral': 'neutral',
                'happy': 'happy',
                'surprised': 'surprised',
                'disgusted': 'disgusted',
                'fearful': 'anxious'
            }

            dominant_mood = mood_mapping.get(dominant_emotion, 'unknown')  # Handle unknown emotions

            # If mood is detected, store the frame
            if dominant_mood != 'unknown':
                detected_frame = frame

        # Check for 'q' key press or capture duration reached
        if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time >= capture_duration:
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    if dominant_mood:
        st.write(f"Detected Dominant Mood: {dominant_mood}")

        # Select appropriate mood dataframes based on the detected mood
        if dominant_mood == 'happy':
            mood_songs_spotify_df = happy_songs_spotify_df
            mood_songs_names_df = happy_songs_names_df
        elif dominant_mood == 'sad':
            mood_songs_spotify_df = sad_songs_spotify_df
            mood_songs_names_df = sad_songs_names_df
        elif dominant_mood == 'angry':
            mood_songs_spotify_df = angry_songs_spotify_df
            mood_songs_names_df = angry_songs_names_df
        elif dominant_mood == 'fear':
            mood_songs_spotify_df = fear_songs_spotify_df
            mood_songs_names_df = fear_songs_names_df
        elif dominant_mood == 'neutral':
            mood_songs_spotify_df = romantic_songs_spotify_df
            mood_songs_names_df = romantic_songs_names_df

        # Display captured frame with detected mood
        if detected_frame is not None:
            st.subheader("Captured Frame with Detected Mood:")
            st.image(detected_frame, channels="BGR", use_column_width=True)

        # Display song recommendations with Spotify links
        st.subheader("Recommended Spotify Songs:")
        for index, row in mood_songs_spotify_df.head(5).iterrows():
            song_name = row['Title']
            spotify_link = row.get('Song URL', 'Not Available')
            st.write(f"Song Name: {song_name}")
            st.write(f"Spotify Link: {spotify_link}")

        st.subheader("Recommended YouTube Songs:")
        for index, row in mood_songs_names_df.head(5).iterrows():
            song_name = row['song']
            artist_name = row['artist']
            youtube_search_query = f"{song_name} {artist_name} {dominant_mood}"
            youtube_search_query_encoded = quote(youtube_search_query)
            youtube_search_link = f"https://www.youtube.com/results?search_query={youtube_search_query_encoded}"
            st.write(f"Song Name: {song_name} by {artist_name}")
            st.markdown(f"YouTube Search Link: [{song_name} on YouTube]({youtube_search_link})")
    else:
        st.warning("No dominant mood detected.")


if __name__ == "__main__":
    main()
