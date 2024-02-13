from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "home"
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/ElvisSandwich.jpg/250px-ElvisSandwich.jpg",
                "title": "Peanut butter, banana and bacon sandwich",
                "description": "The peanut butter and banana sandwich (PB&B), or peanut butter, banana and bacon sandwich (PB,B&B), sometimes referred to as an Elvis sandwich, the Velvet Elvis, or simply the Elvis, is a sandwich with toasted bread, peanut butter, sliced or mashed banana, and occasionally bacon.",
                "reference_url": "https://en.wikipedia.org/wiki/Peanut_butter,_banana_and_bacon_sandwich"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Cheez-It-Crackers.jpg/250px-Cheez-It-Crackers.jpg",
                "title": "Cheez-It",
                "description": "Cheez-It crackers are 26-by-24-millimetre (1.0 by 0.94 in) rectangles, though they are often believed to be squares",
                "reference_url": "https://en.wikipedia.org/wiki/Cheez-It"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Plain-M%26Ms-Pile.jpg/250px-Plain-M%26Ms-Pile.jpg",
                "title": "M&M's",
                "description": "M&M's (stylized as m&m's) are color-varied sugar-coated dragée chocolate confectionery, each of which has the letter \"m\" printed in lower case in white on one side, consisting of a candy shell surrounding a filling which varies depending upon the variety of M&M's",
                "reference_url": "https://en.wikipedia.org/wiki/M%26M%27s"
            },
        ]
        
        return context
    
class AboutPageView(TemplateView):
    template_name='about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_page"] = "about"
        return context
