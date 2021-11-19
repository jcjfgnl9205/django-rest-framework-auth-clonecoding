from django.urls import path
from .views import ExpenseSummaryStatus, IncomeSummaryStatus

urlpatterns = [
    path('expense_category_data', ExpenseSummaryStatus.as_view(), name='expense-category-summary'),
    path('income_source_data', IncomeSummaryStatus.as_view(), name='income_source_data'),
    ]