# from flask import render_template,request,redirect,url_for
# from . import main
# from .forms import PitchForm
# from ..models import Pitch
# from flask_login import login_required
#
# # Views
# @main.route('/')
# def index():
#
#     '''
#     View root page function that returns the index page and its data
#     '''
#     title  = 'Pitch - One Minute Chance to Pitch'
#     search_pitch = request.args.get('pitch_query')
#     pitches = Pitch.get_pitches()
#
#
#     return render_template('index.html', title = title, pitches = pitches)
#
# #
# # @main.route('/pick-up/pitches/')
# # def pick_up():
# #
# #     '''
# #     View movie page function that returns the movie details page and its data
# #     '''
# #     movie = get_movie(id)
# #     title = f'{movie.title}'
# #     reviews = Review.get_reviews(movie.id)
# #
# #     return render_template('movie.html',title = title,movie = movie,reviews = reviews)
# #
# #
# # @main.route('/search/<movie_name>')
# # def search(movie_name):
# #     '''
# #     View function to display the search results
# #     '''
# #     movie_name_list = movie_name.split(" ")
# #     movie_name_format = "+".join(movie_name_list)
# #     searched_movies = search_movie(movie_name_format)
# #     title = f'search results for {movie_name}'
# #     return render_template('search.html',movies = searched_movies)
# #
# #
# # @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# # @login_required
# # def new_review(id):
# #     form = ReviewForm()
# #     movie = get_movie(id)
# #
# #     if form.validate_on_submit():
# #         title = form.title.data
# #         review = form.review.data
# #         new_review = Review(movie.id,title,movie.poster,review)
# #         new_review.save_review()
# #         return redirect(url_for('.movie',id = movie.id ))
# #
# #     title = f'{movie.title} review'
# #     return render_template('new_review.html',title = title, review_form=form, movie=movie)