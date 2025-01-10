from fastapi import APIRouter

router = APIRouter()


@router.get("/install", summary="安装")
async def install():
    """安装"""
    from router import routers

    interfaces = []
    for row in routers:
        for route in row.routes:
            ritem = route.__dict__
            if 'POST' in ritem['methods']:
                interfaces.append({
                    "name": ritem['name'],
                    "path": ritem['path'],
                })

    return {
        "interfaces": interfaces,
    }
