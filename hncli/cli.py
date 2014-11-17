# -*- coding: utf-8 -*-

import click
from click import echo, style

from hn import HN, Story

from hncli._version import __version__


hn = HN()


@click.group()
@click.version_option(__version__)
def cli():
    """ HackerNews CLI - for hackers
    """
    pass


@cli.command()
@click.option('--sort_by', '-s', default='newest',
              type=click.Choice(['newest', 'best']), help='sort type')
@click.option('--limit', '-l', default=10, type=click.INT,
              help='number of top stories to show')
def stories(sort_by, limit):
    """ list stories """
    stories = hn.get_stories(story_type=sort_by, limit=limit)

    if stories:
        echo(style('      when      | comments |   id    | title', fg='yellow'))
    else:
        echo(style('no stories found!', fg='red'))

    for story in stories:
        echo(style(story.published_time.center(15), fg='magenta') + ' | ', nl=False)
        echo(style(str(story.num_comments).center(8), fg='red') + ' | ', nl=False)
        echo(style(str(story.story_id), fg='green') + ' | ', nl=False)
        echo(style(story.title, fg='white'))


@cli.command()
@click.argument('story_id', type=click.INT, required=True)
def go(story_id):
    """ go to the story on HackerNews """
    story = Story.fromid(story_id)
    click.launch(story.link)


@cli.command()
@click.argument('story_id', type=click.INT, required=True)
def comments(story_id):
    """ show comments for the story """
    comments = Story.fromid(story_id).get_comments()

    if not comments:
        echo(style('no coments for story found!', fg='red'))

    for comment in comments:
        echo(style(comment.time_ago.center(15), fg='magenta'), nl=False)
        echo('by ' + style(str(comment.user), fg='cyan'))
        echo(comment.body)


@cli.command()
@click.argument('story_id', type=click.INT, required=True)
def comment(story_id):
    """ comment story on HackerNews """
    story = Story.fromid(story_id)
    click.launch(story.comments_link)


if __name__ == '__main__':
    cli()
