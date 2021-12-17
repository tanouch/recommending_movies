from setuptools import setup, find_packages

if __name__ == "__main__":
    
    setup(
        name = 'recoMovies_SightSound',
        #package_dir={"": "movie_recommendations"},
        #packages=find_packages(where="movie_recommendations"),
        scripts=['movie_recommendations/movie_recommendations.py'],
        include_package_data = True,
        version = '1',
        license='MIT',
        description = 'Recommending movies based on text synopsis using DistilBERT',
        author = 'Ugo Tanielian',
        author_email = 'firstname.lastname@outluuk.fr',  
        url = 'https://github.com/tanouch/recommending_movies',
        entry_points={"console_scripts": ["recoMovies_SightSound = movie_recommendations:get_movie_recommendations"]},
        keywords = ['NLP', 'movies'],
        install_requires=[
            "numpy",
            "wikipedia",
            "transformers",
            "torch", 
            "fire",
            "scipy"
        ],
        classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        ]
    )