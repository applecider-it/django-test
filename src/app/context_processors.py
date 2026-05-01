from .vite import ViteCtrl

def my_context(request):
    return {
        "vite": ViteCtrl()
    }