from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import pika
import json
# Create your views here.

@csrf_protect
@csrf_exempt
def add_item(request):
	
	if request.method == "POST":
		# postdata = request.POST.copy()
		# item_name = postdata.get('item',None)


		# To check if json data is passed
		try:
			raw_json = request.body.decode('utf-8')
			raw_json_data = json.loads(raw_json)
		except ValueError as e:
			print(e)
			response = {'status' : 'error','message':"Please Pass Raw Json Data"}
			return JsonResponse(response)


		item_name = raw_json_data.get('item',None)

		# If item is not passed
		if item_name == None:
			response = {'status' : 'error','message':"please add item"}
			return JsonResponse(response)

		# To check if item already present in database
		try:
			item_obj  = get_object_or_404(items,item=item_name)
		except:
			item_obj  = None

		# If not present in database then add item 
		if item_obj == None:
			item_obj = items()
			item_obj.item = item_name
			item_obj.status = "pending"
			item_obj.save()
			data = {'item' : item_name,}   

			message = json.dumps(data)

			# Make connection to rabbitMQ and add message 
			connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
			channel = connection.channel()
			channel.queue_declare(queue='queueName')
			channel.basic_publish(exchange='', routing_key='queueName', body=message, properties='')
			print("Sent to rabbitMQ queue")
			connection.close()

			response = {'status' : 'success','status_code' : 202,'message':"",'data':data}

		# If item already present return error
		else:
			response = {'status' : 'error','message':"item already exists"}
		return JsonResponse(response)

	response = {'status' : 'error','message':"something went wrong",}
	return JsonResponse(response)


def view_items(request):
	item_obj2  = items.objects.all()
	items_list = []
	for nm in item_obj2:
		temp = {
			'id':nm.id,
			'item':nm.item,
			'status':nm.status
		}
		items_list.append(temp)
	response = {'status' : 'success','message':"",'data':items_list}
	return JsonResponse(response)


def delete_items(request,item_name):
	try:
		item_obj  = items.objects.get(item=item_name)
	except:
		item_obj = None
	if item_obj:
		item_obj.delete()
		response = {'status' : 'success','message':"item deleted"}
	else:
		response = {'status' : 'error','message':"item not present"}
	return JsonResponse(response)