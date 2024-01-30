from fastapi import APIRouter, Depends, HTTPException
from db import database

router_usuarios = APIRouter()


@router_usuarios.post("/register/user/", tags=["Usuarios"])
async def register(us_cedula: str, us_nombres: str, us_apellidos: str, us_email: str, us_contrasenia: str):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = '''
                    INSERT INTO usuario (
	                    us_cedula, 
                        us_nombres, 
                        us_apellidos, 
                        us_email, 
                        us_contrasenia, 
                        us_estado, 
                        us_fecha_bd
                    )   VALUES (
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        'A', 
                        now()
                    ) RETURNING
                        us_cedula, 
                        us_nombres, 
                        us_apellidos, 
                        us_email, 
                        us_contrasenia, 
                        us_estado, 
                        us_fecha_bd;
                '''

        cursor.execute(query, (us_cedula, us_nombres, us_apellidos, us_email, us_contrasenia))
        detalle_usuario = cursor.fetchone()

        conn.commit()
        conn.close()

        if detalle_usuario:
            usuario = {
                "us_cedula": detalle_usuario[0],
                "us_nombres": detalle_usuario[1],
                "us_apellidos": detalle_usuario[2],
                "us_email": detalle_usuario[3],
                "us_contrasenia": detalle_usuario[4],
                "us_estado": detalle_usuario[5],
                "us_fecha_bd": detalle_usuario[6],
            }
            return{
                    "mensaje": "Usuario registrado correctamente", 
                    "Usuario": usuario
            }, 200
        else:
            return HTTPException(
                status_code=401, detail="Error al obtener los datos del usuario creado."
            )

    except Exception as e:
        return {
            "error": 'Error al crear usuario', "message": str(e)
        }, 404
    
@router_usuarios.post("/login/", tags=["Usuarios"])
async def login(us_email: str, us_contrasenia: str):
    try:
        conn = database.getConnection()
        cursor = conn.cursor()

        query = '''
                    SELECT
	                    us_cedula, 
                        us_nombres, 
                        us_apellidos, 
                        us_email, 
                        us_contrasenia, 
                        us_estado, 
                        us_fecha_bd
                    FROM 
                        usuario
                    WHERE
                        us_email = %s AND 
                        us_contrasenia = %s
                '''

        cursor.execute(query, (us_email, us_contrasenia))
        detalle_usuario = cursor.fetchone()

        conn.close()

        if detalle_usuario:
            usuario = {
                "us_cedula": detalle_usuario[0],
                "us_nombres": detalle_usuario[1],
                "us_apellidos": detalle_usuario[2],
                "us_email": detalle_usuario[3],
                "us_contrasenia": detalle_usuario[4],
                "us_estado": detalle_usuario[5],
                "us_fecha_bd": detalle_usuario[6],
            }
            return {
                    "mensaje": "Login exitoso.", 
                    "Usuario": usuario
            }, 200
        else:
            raise HTTPException (
                status_code=404, detail="Error de acceso. Verifica las credenciales y vuelve a intentarlo."
            )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Error interno del servidor"+str(e)
        )
