from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.templatetags.staticfiles import static as _static
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django_nyt.urls import get_pattern as get_nyt_pattern
from wiki.urls import get_pattern as get_wiki_pattern

from django.contrib import admin

from pinaxcon import views

import symposion.views


urlpatterns = [
    url(r"^/$", TemplateView.as_view(template_name="static_pages/homepage.html"), name="home"),

    # about
    url(r"^about/north-bay-python/$", TemplateView.as_view(template_name="static_pages/about/north_bay_python.html"), name="about/north-bay-python"),
    url(r"^about/petaluma/$", TemplateView.as_view(template_name="static_pages/about/petaluma.html"), name="about/petaluma"),
    url(r"^about/team/$", TemplateView.as_view(template_name="static_pages/about/team.html"), name="about/team"),
    url(r"^about/transparency/$", TemplateView.as_view(template_name="static_pages/about/transparency/transparency.html"), name="about/transparency"),
    url(r"^about/program-transparency/$", TemplateView.as_view(template_name="static_pages/about/transparency/program.html"), name="about/program-transparency"),
    url(r"^about/colophon/$", TemplateView.as_view(template_name="static_pages/about/colophon.html"), name="about/colophon"),

    # program
    url(r"^program/events/$", TemplateView.as_view(template_name="static_pages/program/events.html"), name="program/events"),
    url(r"^events/$", RedirectView.as_view(url="program/events")),
    url(r"^program/call-for-proposals/$", RedirectView.as_view(url="/speak")),
    url(r"^program/selection-process/$", TemplateView.as_view(template_name="static_pages/program/selection_process.html"), name="program/selection-process"),
    url(r"^proposals/$", RedirectView.as_view(url="/speak")),
    url(r"^cfp/$", RedirectView.as_view(url="/speak")),
    url(r"^speak/$", TemplateView.as_view(template_name="static_pages/speak.html"), name="speak"),

    # attend
    # url(r"^attend$", TemplateView.as_view(template_name="static_pages/attend/attend.html"), name="attend/attend"),
    url(r"^tickets/$", RedirectView.as_view(url="attend")),
    url(r"^tickets/buy/$", views.buy_ticket, name="buy_ticket"),
    url(r"^attend/business-case/$", TemplateView.as_view(template_name="static_pages/attend/business-case.html"), name="attend/business-case"),

    url(r"^opportunity-grant/$", TemplateView.as_view(template_name="static_pages/opportunity-grant.html"), name="opportunity-grant"),
    url(r"^attend/finaid/$", RedirectView.as_view(url="/opportunity-grant")),
    url(r"^attend/finaid/$", RedirectView.as_view(url="/opportunity-grant")),
    url(r"^attend/financial-aid/$", RedirectView.as_view(url="/opportunity-grant")),

    # url(r"^attend/stay/$", TemplateView.as_view(template_name="static_pages/attend/travel.html"), name="attend/travel"),
    # url(r"^attend/travel/$", TemplateView.as_view(template_name="static_pages/attend/travel.html"), name="attend/travel"),
    url(r"^attend/hotels/$", TemplateView.as_view(template_name="static_pages/attend/hotels.html"), name="attend/hotels"),
    # url(r"^attend/tshirt/$", TemplateView.as_view(template_name="static_pages/attend/tshirt.html"), name="attend/tshirt"),
    url(r"^attend/accessibility-and-accommodations/$",TemplateView.as_view(template_name="static_pages/attend/accommodations.html"), name="attend/accessibility-and-accommodations"),
    url(r"^accessibility/$", RedirectView.as_view(url="attend/accessibility-and-accommodations")),
    url(r"^accommodations/$", RedirectView.as_view(url="attend/accessibility-and-accommodations")),
    url(r"^a11y/$", RedirectView.as_view(url="attend/accessibility-and-accommodations")),
    url(r"^guides/$",TemplateView.as_view(template_name="static_pages/attend/guides.html"), name="attend/guides"),
    url(r"^guide/$", RedirectView.as_view(url="guides")),

    # go
    url(r"^go/fly/$", TemplateView.as_view(template_name="static_pages/go/fly.html"), name="go/fly"),
    url(r"^go/stay/$", TemplateView.as_view(template_name="static_pages/go/stay.html"), name="go/stay"),
    url(r"^go/day-trip/$", TemplateView.as_view(template_name="static_pages/go/day-trip.html"), name="go/day-trip`"),

    url(r"^safety/$", TemplateView.as_view(template_name="static_pages/safety.html"), name="safety"),
    url(r"^emergencies/$", RedirectView.as_view(url="safety")),
    url(r"^emergency/$", RedirectView.as_view(url="safety")),

    url(r"^attend/food/$", TemplateView.as_view(template_name="static_pages/attend/food.html"), name="attend/food"),
    url(r"^food-guide/$", RedirectView.as_view(url="attend/food")),
    url(r"^food/$", RedirectView.as_view(url="attend/food")),
    url(r"^attend/transit/$", TemplateView.as_view(template_name="static_pages/attend/transit.html"), name="attend/transit"),
    url(r"^transit/$", RedirectView.as_view(url="attend/transit")),

    url(r"^code-of-conduct/$", TemplateView.as_view(template_name="static_pages/code_of_conduct/code_of_conduct.html"), name="code-of-conduct"),
    url(r"^coc/$", RedirectView.as_view(url="code-of-conduct")),
    url(r"^code-of-conduct/harassment-incidents/$", TemplateView.as_view(template_name="static_pages/code_of_conduct/harassment_procedure_attendee.html"), name="code-of-conduct/harassment-incidents"),
    url(r"^code-of-conduct/harassment-staff-procedures/$", TemplateView.as_view(template_name="static_pages/code_of_conduct/harassment_procedure_staff.html"), name="code-of-conduct/harassment-staff-procedures"),
    url(r"^terms-and-conditions/$", TemplateView.as_view(template_name="static_pages/terms_and_conditions.html"), name="terms-and-conditions"),
    url(r"^terms/$", RedirectView.as_view(url="terms-and-conditions")),

    # sponsor
    url(r"^sponsors/prospectus/$", RedirectView.as_view(url=_static("assets/northbaypython_prospectus.pdf")), name="sponsors/prospectus"),
    url(r"^northbaypython_prospectus.pdf$", RedirectView.as_view(url=_static("assets/northbaypython_prospectus.pdf")), name="northbaypython_prospectus.pdf"),
    url(r"^sponsors/become-a-sponsor/$", TemplateView.as_view(template_name="static_pages/sponsors/become_a_sponsor.html"), name="sponsors/become-a-sponsor"),
    url(r"^sponsors/donate/$", TemplateView.as_view(template_name="static_pages/sponsors/donate.html"), name="sponsors/donate"),
    url(r"^donate/$", RedirectView.as_view(url="sponsors/donate")),
    url(r"^about/donate/$", RedirectView.as_view(url="sponsors/donate")),

    # news
    url(r"^news/$", TemplateView.as_view(template_name="static_pages/news.html"), name="news"),

    # Django, Symposion, and Registrasion URLs

    url(r"^admin/", include(admin.site.urls)),

    url(r"^login$", views.account_login, name="nbpy_login"),
    # Override the default account_login view with one that takes email addys
    url(r"^account/login/$", views.EmailLoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),

    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^reviews/", include("symposion.reviews.urls")),
    url(r"^schedule/", include("symposion.schedule.urls")),

    url(r"^teams/", include("symposion.teams.urls")),

    # Demo payment gateway and related features
    url(r"^tickets/payments/", include("registripe.urls")),

    # Required by registrasion
    url(r'^tickets/', include('registrasion.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),

    url(r'^wiki/notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())

    # Catch-all MUST go last.
    #url(r"^", include("pinax.pages.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = views.server_error
