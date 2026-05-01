import json
from pathlib import Path
from django.conf import settings

class ViteCtrl:
    """Vite管理"""

    def __init__(self):
        # マニフェストのキャッシュ
        self.manifest = None

    def init(self) -> str:
        """Viteを使用する準備"""
        val = ""

        if self.is_dev():
            val = f'<script type="module" src="{self.dev_url()}/@vite/client"></script>'

        return val

    def asset(self, entry: str) -> str:
        """Viteアセットのパスをmanifestから返す。"""
        if self.is_dev():
            return f"{self.dev_url()}/{entry}"
        else:
            self.init_manifest()
            return f"/assets/{self.manifest[entry]['file']}"

    def init_manifest(self):
        """Manifestを取得"""
        if self.manifest is None:
            path = Path(SFW_PROJECT_ROOT) / "public/assets/.vite/manifest.json"
            with open(path, encoding="utf-8") as f:
                self.manifest = json.load(f)

    def is_dev(self) -> bool:
        """Viteが開発環境か返す"""
        return settings.VITE['dev']

    def dev_url(self) -> str:
        """開発環境のURL"""
        return f"http://localhost:{settings.VITE['port']}"
