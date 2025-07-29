from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import get_connection
from .models import Room

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Создание записи через ORM
            room = Room.objects.create(
                number=data['number'],
                floor=data['floor'],
                capacity=data['capacity']
            )

            return JsonResponse({'id': room.id, 'message': 'Room created'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            room_id = data.get('id')
            if not room_id:
                return JsonResponse({'error': 'Room ID is required'}, status=400)

            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM rooms WHERE id = %s;", (room_id,))
            conn.commit()
            cur.close()
            conn.close()

            return JsonResponse({'message': f'Room with ID {room_id} deleted'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
