from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from .models import Skill, Project, Publication


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['skills_by_category'] = self._grouped_skills()
        ctx['projects'] = Project.objects.all()
        ctx['publications'] = Publication.objects.all()
        return ctx

    def _grouped_skills(self):
        order = [
            'Programming Languages',
            'Python GIS/ML Libraries',
            'GIS & Esri Technologies',
            'Web & App Development',
            'Cloud & Infrastructure',
            'Tools',
        ]
        groups = {}
        label_map = dict(Skill.CATEGORY_CHOICES)
        for skill in Skill.objects.all():
            label = label_map.get(skill.category, skill.category)
            groups.setdefault(label, []).append(skill.name)
        # pair every two skills: "GDAL / Rasterio"
        paired = {}
        for label in order:
            if label in groups:
                names = groups[label]
                paired[label] = [
                    f"{names[i]} / {names[i+1]}" if i+1 < len(names) else names[i]
                    for i in range(0, len(names), 2)
                ]
        return paired

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
        else:
            messages.error(request, "Please fill in all fields.")
        return redirect('core:home')
