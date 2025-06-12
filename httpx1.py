# import httpx
# data = {'integer' : 123, 'boolean': True,'list' : ['a','b','c']}
# r = httpx.post('https://httpbin.org/post',json=data)


# import httpx
# with httpx.Client() as client:
#     r = client.get('https://example.com')

import httpx

async with httpx.AsyncClient() as client:
    response = await client.get('https://example.com')
    print response

asyncio.run(main())