# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import werkzeug
import itertools
import pytz
import babel.dates
from collections import OrderedDict

from odoo import http, fields, _
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.website import slug, unslug
from odoo.exceptions import UserError
from odoo.http import request
from odoo.tools import html2plaintext
from odoo.addons.website_blog.controllers.main import WebsiteBlog

class LatestBlogPostController(WebsiteBlog):
    @http.route('/snippet/get_latest_blog_post_list', type='http', auth='public', website=True)
    def get_latest_blog_post_list(self, number, **post):
        print number
        Event = request.env['blog.post']
        result = {'events': []}
        events = None

        events = Event.search([('website_published', '=', True)], limit=number, order="create_date desc")

        for event in events:
            create_date_arr = event.create_date.split(" ")[0].split("-")
            create_date = create_date_arr[2] + "/" + create_date_arr[1] + "/" + create_date_arr[0]
            result['events'].append({
                "event": event,
                "create_date": create_date
            })
        # return request.render("latest_blog_post_snippet.latest_blog_post_list", result)