import json
from pathlib import Path
from django.conf import settings
from typing import Optional, Dict, Any
from django.templatetags.static import static

class ViteCtrl:
    """Vite管理クラス"""

    def __init__(self) -> None:
        self.is_dev: bool = settings.VITE['dev']
        self.dev_url: str = f"http://localhost:{settings.VITE['port']}"
        self.prod_url: str = "build"
        self.manifest: Optional[Dict[str, Any]] = {}

        manifest_path = settings.BASE_DIR / "static/build/.vite/manifest.json"

        if not self.is_dev:
            with open(manifest_path, "r", encoding="utf-8") as f:
                self.manifest = json.load(f)

    def init(self) -> str:
        """初期処理"""
        if self.is_dev:
            url = f"{self.dev_url}/@vite/client"
            return self._import_js_tag(url)
        else:
            return ""

    def import_js(self, path: str) -> str:
        """JSからの読み込み"""
        if self.is_dev:
            url = f"{self.dev_url}/{path}"
            return self._import_js_tag(url)
        else:
            data = self.manifest[path]
            url = static(f"{self.prod_url}/{data['file']}")
            html = self._import_js_tag(url)

            # JSから読み込むときに、CSSの読み込みもある場合があるのでその対応
            if "css" in data:
                for css in data["css"]:
                    css_url = static(f"{self.prod_url}/{css}")
                    html += self._import_css_tag(css_url)

            return html

    def import_css(self, path: str) -> str:
        """CSSからの読み込み"""
        if self.is_dev:
            url = f"{self.dev_url}/{path}"
            return self._import_css_tag(url)
        else:
            data = self.manifest[path]
            url = static(f"{self.prod_url}/{data['file']}")
            return self._import_css_tag(url)

    def _import_js_tag(self, url: str) -> str:
        return f'<script type="module" src="{url}"></script>'

    def _import_css_tag(self, url: str) -> str:
        return f'<link rel="stylesheet" href="{url}" type="text/css" media="all" />'
