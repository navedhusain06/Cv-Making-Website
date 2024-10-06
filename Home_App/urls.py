from django.urls import path
from .views import *

urlpatterns = [
    path('', homeFun, name='homeNm'),
    path('coverletter/', homeSecondFun, name='homeSecondNm'),
    path('cv/', cvTemplateFun, name='cvTemplateNm'),
    # path('cvShow/', cvTemplateShowFun, name='cvTemplateShowNm'),
    
    # DOWNLOAD
    
   path('download_cv/<int:cv_id>/', download_cv, name='download_cv'),
]