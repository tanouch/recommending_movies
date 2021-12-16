from setuptools import setup, find_packages

if __name__ == "__main__":
    
    setup(
      name = 'movie_recommendation_sight_and_sound',
      packages = find_packages(),
      include_package_data = True,
      version = '1',
      license='MIT',
      description = 'Recommending movies based on text synopsis using DistilBERT',
      authors = 'Ugo Tanielian',
      url = 'https://github.com/tanouch/synthetic_gans',
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
      ],
    )