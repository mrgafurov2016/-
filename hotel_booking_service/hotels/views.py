from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .db import get_connection

@csrf_exempt
def create_room(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO rooms (number, floor, capacity) VALUES (%s, %s, %s) RETURNING id;",
                (data['number'], data['floor'], data['capacity'])
            )
            room_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            return JsonResponse({'id': room_id, 'message': 'Room created'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
