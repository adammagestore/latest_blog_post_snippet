# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Latest Blog Post Snippet',
    'category': 'Website',
    'sequence': 240,
    'website': 'https://www.odoobin.com',
    'summary': 'News, Blogs, Announces, Discussions',
    'version': '1.0',
    'description': """
Odoo Latest Blog Post Snippet
============

        """,
    'depends': ['website_blog'],
    'data': [
        'views/latest_blog_post_templates.xml',
        'views/latest_blog_post_snippets.xml',
    ],
    'demo': [

    ],
    'test': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
