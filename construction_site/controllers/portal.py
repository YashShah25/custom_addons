from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.http import request
from collections import OrderedDict


class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['count_sites'] = request.env['construction.site'].search_count([])
        print("\n\n\n\n////////////values : ", values)
        return values

    @http.route(['/my/construction_site'], type='http', auth="user", website=True)
    def portal_my_construction_site(self, page=1, sortby=None, filterby=None, **kw):
        values = self._prepare_portal_layout_values()
        ConstructionSite = request.env['construction.site']

        searchbar_sortings = {
            'scheduled_date': {'label': _('Scheduled Date'), 'order': 'scheduled_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'state'},
        }
        # default sortby order
        if not sortby:
            sortby = 'scheduled_date'
        sort_order = searchbar_sortings[sortby]['order']

        searchbar_filters = {
            'all': {'label': 'All', 'domain': []},
            'draft': {'label': 'Draft', 'domain': [('state', '=', 'draft')]},
        }
        # default filter by value
        domain = []

        if not filterby:
            filterby = 'all'
        domain += searchbar_filters[filterby]['domain']
        print("\n\n\ndomain = ", domain)

        # count for pager
        count_sites = ConstructionSite.search_count(domain)

        # make pager
        pager = portal_pager(
            url="/my/construction_site",
            url_args={'sortby': sortby, 'filterby': filterby},
            total=count_sites,
            page=page,
            step=self._items_per_page
        )

        # search the count to display, according to the pager data
        sites = ConstructionSite.search(
            domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_construction_history'] = sites.ids[:100]
        for s in sites:
            print("\n\n\nsites = ", s)
        print("\n\n\nsites = ", sites)

        values.update({
            'sites': sites,
            'page_name': 'site',
            'pager': pager,
            'default_url': '/my/construction_site',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })

        return request.render("construction_site.portal_my_construction", values)

    @http.route(
        "/site/info/<model('construction.site'):site_id>",
        type="http",
        website=True,
        auth="public",
    )
    def form_page(self, site_id, page=1, **kw):
        values = self._prepare_portal_layout_values()
        values.update({'site_id': site_id,
                       'page_name': 'site_info',
                       })
        print('\n\n\n\nvalues = ', values)
        return request.render(
            "construction_site.site_info", values
        )
