import json
from rest_framework.renderers import JSONRenderer



class CatJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):

        if len(data) == 0:
            return super(CatJSONRenderer, self).render(data)

        return json.dumps({'cats': data})
