from datetime import date
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from home.models import TaskInstance

dt = date.today()
today_start = datetime.combine(dt, datetime.min.time())

DAG_ID 		= "ethereum_export_dag"
NW_DAG_ID 	= "nodewatch_ethereum_export_dag"

class DAGRunView(View):
	def get(self, request, *args, **kwargs):
		template 		= "home.html"
		dag_num_succ 	= TaskInstance.objects.filter(dag_id=DAG_ID,
												state='success',
												start_date__gte=today_start
												).count()
		dag_num_rty 	= TaskInstance.objects.filter(dag_id=DAG_ID,
												state='up_for_retry',
												start_date__gte=today_start
												).count()
		dag_num_run 	= TaskInstance.objects.filter(dag_id=DAG_ID,
												state='running',
												start_date__gte=today_start
												).count()

		nw_num_succ 	= TaskInstance.objects.filter(dag_id=NW_DAG_ID,
												state='success',
												start_date__gte=today_start
												).count()
		nw_num_rty 		= TaskInstance.objects.filter(dag_id=NW_DAG_ID,
												state='up_for_retry',
												start_date__gte=today_start
												).count()
		nw_num_run 		= TaskInstance.objects.filter(dag_id=NW_DAG_ID,
												state='running',
												start_date__gte=today_start
												).count()
		context 	= {
							'dag_num_succ' 	: dag_num_succ,	
							'dag_num_rty' 	: dag_num_rty,
							'dag_num_run' 	: dag_num_run,	
							'nw_num_succ' 	: nw_num_succ,	
							'nw_num_rty' 	: nw_num_rty ,
							'nw_num_run' 	: nw_num_run 
						}
		if request.is_ajax():
			return HttpResponse(context, content_type="application/json")
		return render(request, template, context)
