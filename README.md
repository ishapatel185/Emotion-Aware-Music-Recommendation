
# Emotion Aware Music Recommendation
The "Emotion Aware Music Recommendation" system is a web application that offers personalized music suggestions based on the user's mood. Using facial emotion recognition, it analyzes the user's expressions via webcam to identify emotions and recommends five relevant songs from YouTube and Spotify.


## Dataset
Top 200 Spotify Songs Dataset: This dataset provides insights into the top 200 songs on Spotify, including features like audio attributes and popularity. (https://www.kaggle.com/datasets/brunoalarcon123/top-200-spotify-songs-dataset)

Spotify Million Song Dataset: A comprehensive collection of a million songs from Spotify, featuring various audio characteristics and metadata for music analysis. (https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

Facial Expression Image Dataset: This dataset contains images of facial expressions, used for training emotion recognition models. (https://www.kaggle.com/datasets/msambare/fer2013)

## User Interface
The user interface, built with Streamlit, captures a 5-second video of the user to assess their mood. Utilizing facial emotion recognition, the system then curates and recommends 5 songs, providing direct links to both YouTube and Spotify for seamless listening.

## Screenshots
![isha_happy](https://github.com/user-attachments/assets/f4aa7a7e-b2a2-457f-a889-c4e6d92a6dfa)



![nisha_sad](https://github.com/user-attachments/assets/fcebe89c-6caa-4014-ba10-7bc924ea55aa)


## Technologies Used
Python

Streamlit

OpenCV

DeepFace

Pandas

URL Parsing


## References
[1]	Parmar, P. H. (2020). Music Recommendation System Using Facial Expression Recognition (Master's thesis). Birla Vishvakarma Mahavidyalaya (Engineering 
	College), 	An 	Autonomous 	Institution 	affiliated 	to GujaratTechnologicalUniversity  
  	https://bvmengineering.ac.in/NAAC/Criteria1/1.3/1.3.4/18CP807_Thesis.pdf
  
[2]	Koelstra, S., Muhl, C., Soleymani, M., Lee, J.S., Yazdani, A., Ebrahimi, T., Pun, T., Nijholt, A., & Patras, I. (2011). DEAP: A Database for Emotion Analysis; Using Physiological Signals. IEEE 		Transactions on Affective Computing, 3(1), 18-31. (https://ieeexplore.ieee.org/document/5589328) 

[3]	Yang, Y., Wang, X., & Chen, L. (2014). Music Emotion Recognition: A State of the Art Review. IEEE Transactions on Affective Computing, 5(4), 1-1. (https://ieeexplore.ieee.org/document/6703570 
