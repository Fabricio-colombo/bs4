import requests
from bs4 import BeautifulSoup as bs
import time
from config import login_conf, senha_conf

session = requests.Session()

def login_safra(login, senha, session):
    url = 'https://epfweb.safra.com.br/Home/Login'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://epfweb.safra.com.br/Home/Login",
        "Origin": "https://epfweb.safra.com.br",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,pt;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest"
    }
    response = session.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    verification_token = soup.find('input', {'name': '__RequestVerificationToken'})['value']
    data = {
        '__RequestVerificationToken': verification_token,
        'login': login,
        'senha': senha,
    }
    response = session.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(response.text)
        print("Solicitação bem-sucedida!")
        print(f"__RequestVerificationToken:", verification_token, end='\n\n')
        cookies_dict = session.cookies.get_dict()
        print("Cookies da sessão:", cookies_dict, end='\n\n')
        
        cookie_values = {}
        for key, value in cookies_dict.items():
            cookie_values[key] = value

        _abck = cookies_dict.get('_abck', '')
        ak_bmsc = cookies_dict.get('ak_bmsc', '')
        bm_mi = cookies_dict.get('bm_mi', '')
        bm_sv = cookies_dict.get('bm_sv', '')
        bm_sz = cookies_dict.get('bm_sz', '')
        NSC_WJQ_GJOBODFJSB_FQGXFC_443 = cookies_dict.get('NSC_WJQ_GJOBODFJSB_FQGXFC_443', '')
        __RequestVerificationToken = cookies_dict.get('__RequestVerificationToken', '')

        notifier = "notifier=toastr" + "; "
        __RequestVerificationToken = "__RequestVerificationToken=" + __RequestVerificationToken + "; "
        NSC_WJQ_GJOBODFJSB_FQGXFC_443 = "NSC_WJQ_GJOBODFJSB_FQGXFC_443=" + NSC_WJQ_GJOBODFJSB_FQGXFC_443 + "; "
        bm_mi = "bm_mi=" + bm_mi + "; "
        ak_bmsc = "ak_bmsc=" + ak_bmsc + "; "
        bm_sv = "bm_sv=" + bm_sv + "; "
        bm_sz = "bm_sz=" + bm_sz  #lembrar de tirar o ; em alguns casos quando ele for o ultimo
        ASP_NET_SessionId = "ASP.NET_SessionId=" + "; "
        # .ASPXAUTH=
        _abck = "_abck=" + _abck + "; "

        print(__RequestVerificationToken, end='\n\n')
        print(NSC_WJQ_GJOBODFJSB_FQGXFC_443, end='\n\n')
        print(ak_bmsc, end='\n\n')
        print(bm_sv, end='\n\n')
        print(bm_sz, end='\n\n')
        print(_abck, end='\n\n')
        print(ASP_NET_SessionId, end='\n\n')

        return _abck, ak_bmsc, bm_mi, bm_sv, bm_sz, NSC_WJQ_GJOBODFJSB_FQGXFC_443, __RequestVerificationToken, verification_token, notifier, session, ASP_NET_SessionId
    else:
        print("Erro ao efetuar o login. Código de status:", response.status_code)
        return None


def cookies_safra(login, senha, verification_token, session, __RequestVerificationToken, NSC_WJQ_GJOBODFJSB_FQGXFC_443, _abck, ak_bmsc, bm_sv, bm_sz, ASP_NET_SessionId, notifier, bm_mi):
    url = 'https://epfweb.safra.com.br/Home/Logar'
    print(notifier + __RequestVerificationToken + bm_mi + ak_bmsc + NSC_WJQ_GJOBODFJSB_FQGXFC_443 + _abck + ASP_NET_SessionId + bm_sv + bm_sz, end='\n\n')
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Referer": "https://epfweb.safra.com.br/Home/Login",
        "Origin": "https://epfweb.safra.com.br",
        "Sec-Ch-Ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,pt;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "notifier=toastr; __RequestVerificationToken=Qs-kz_drlpXvnMR1wkWIPqerLWDfyQCtIqi3VxF2hNYpu7KvK4As9vjHOVxixqQZ7e6LiJ8fjP_toElwf5GJknEX4Z-x2NZhP8BXGuMPdt6fssseQ5FSy-bEYrsLiJIridW4EDPYDfRg2Cwlga9Q1Q2; bm_mi=A99A6AC2A52931B64423B31D0D9C04F0~YAAQtA8tFy0iAaCOAQAAxQv7rheIK8/AX2b6AW/PyswIx4QfudSEBSydxVbVnQTqUeOPysH5yhxr9YysJLgKjQgwoORbLRGZtosMxhLRO1oY16cP0QeJZw7MDrZIbeiakddfTtF24tDgCo0/KRqVawws08yjS9gahVDSYSmPBMsnoUkgQuY+u928uv2aUPkLcRWnEDaZaktF3uXw7avoGAUIQfynDVs2Bgti4e2dtxFfBrHAArPT0sIiJLEa2U5Sc4vyoazEHkEHN3yNsw5Ge5GVaeSlQXdrUg4bb54VMuppBGN+HRoWGEXjUytggvZIDviC1GyauiyQ~1; ak_bmsc=A1B616D48BB9DA7E0764F6C054D5103B~000000000000000000000000000000~YAAQtA8tF04iAaCOAQAA8Q77rhfYP7gQJkSpltFAJowYnrwecp3sfuIFlufO46M6zZD7mXqfpoxABwmiu0mhAHsiHL76o+YC7zpYS2u31rCmgDrCIEXNN00XD5EocX7xJrTVpWONewusd/L0kD8jufW5CyattxOBQKbCFCe0olbInz2/Yb2gkvIjxcsbUTj4X4JdfK4f1+cDVWbaW5W9Qv/5nBGalWZfOP7rbQj4hQ+efekMBPfKgebYfhy3mrlpkNVpGLisNNLAyC9lfZ16FYUFB1f/R4CxvnM/rcFvedJLh+XqcxVrwt+Z+aJclTN3Akk5qxXvQr4RnPo4BihZ80kThBveq7D1TjqbgUKDt+v2qR8lY0e7klx9GeLsJIAuD7kcrttr7PYvs42dKbXVi1/fYpisTPUk04e59FUORtj3XcTvuAr7BX4tNBeyUJTEHO5C5AJqcLAx4J/2D1aJSndmJdy2L88nb3GjupWGh4ihqvHJhHx4GxVS; NSC_WJQ_GJOBODFJSB_FQGXFC_443=ffffffffaf19191d45525d5f4f58455e445a4a42378b; _abck=8BFA4632C489C14A49C6CFDE3F0D089E~0~YAAQdQ8tF+HdJpmOAQAAowcFrwvWPYPmghVUKDFoFgTKcg6uscPFF0b5EOr09tu2FQeOkStlyPUXjw5BsUwXJWXvfB2A1gaI+7SlGQ8QNHu+Te8o/KjnUdoxfWlYBStyZ0XWtGdAhhQfEMO01kj7aKRl+Z+cB7isCHgzxlGQFhwKn0K0fA/LIfT4dJcjlYZ2ilKsdN2njv58RgzpjdtR9ZLaI4EQi4RKsODYMYP7xLy529Qoa5RGpLvWPkhhyxHRN1TubksX/4JZ07/HlHVx33gS0zd7wqnPGiwe5e3RTX4oVj4h8GysvgO4yG159l+DT61iUY6hS6hJmZgdM7BILlymHUVtAPCiWvj6pN2UjDPpOP8noVL6d9pCXJlbsOIeOnVnsVMjfqoeB73zEQe+TpzRhGyBKDDpEg==~-1~-1~-1; ASP.NET_SessionId=; bm_sv=B7D6B82CC0635FBF072C3B6DEA457ECC~YAAQdQ8tF9HkJpmOAQAA+ooFrxfvsJIdz9WDuSZn/dXsbRhj5r++OVOPHu9b0/wAd9mxLWSDAzw8xzxVWQ6L8L5cZfe1UuMx/R6xZ77HdHH3Xxzwm8H/zHOvLkUEVMFKL4OvtwB4AgRdFOnx3L/A0M6Gyxy13U3Vg2KujTQC1MD2khqgULfkZOc6k/r7hvOVu1LpkSJ3P8/WjCz9/vhvc3Ry8aqdkRYjBFVF350PbPHDwgpAgRn2qBXIkzIsF7QAXzs+~1; bm_sz=FA55714DA7BC30046D1AD65EB2B2F4FF~YAAQdQ8tF9LkJpmOAQAA+ooFrxevC/1ppGQgKZtqrymMIvcswhqYCuplPFTj3w+kxKVRKWFLCiMwHutp6faTpb8o8LjObFqkpsA8uqBeCU/+A+xiJ2NGkG6FMmvjuFyWZ+65+O2r5RbkhYdZIuG4D967MRD+VPsibrP/3g+IemTlxtCVBa/Gv865DvPDsEhPwvKGAwcf5gjzqwlniEizKn1Ctz8fgxNX7iLLI7jZLvIM4Hzl58ROl8WjXO70q6Hwzpzta1BYJxi8+7dhFhT5tQ/RSm4HMF9lJcSYDdbVTxNXNexzrMEkYQ/z4RmZh+1mHQDYStAhBmK9ZcjmgbuZnRdao+sAqs6KFpx0evDxABmzFgpJ6d1Zt0u7epMpbTxHkVhNf7RR+rlZn/b6LLg81zshDyjc1X94xrzmfDqNGh/OWypVZbmqjclu0QTS0Rs8ZpVOwA9qbEDv4Kqkh+9CBMXJyniS30prAWLIYWz3Yg==~3688002~3552066",
        #"Cookie": notifier + __RequestVerificationToken + bm_mi + ak_bmsc + NSC_WJQ_GJOBODFJSB_FQGXFC_443 + _abck + ASP_NET_SessionId + bm_sv + bm_sz
    }
    #notifier=toastr;
        #__RequestVerificationToken
        #bm_mi
        #ak_bmsc
        #NSC_WJQ_GJOBODFJSB_FQGXFC_443
        #_abck
        #ASP.NET_SessionId
        #bm_sv
        #bm_sz
    payload = {
        "__RequestVerificationToken": verification_token,
        "IsInterno": "true",
        "Usuario.DsLogin": login,
        "Senha": senha,
        "CEP": "",
        "responseCaptcha": ""
    }
    response = session.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        cookies = response.cookies
        asp_net_session_id = cookies.get('ASP.NET_SessionId', '')
        aspxauth = cookies.get('.ASPXAUTH', '')

        print("ASP.NET_SessionId:", asp_net_session_id, end='\n\n')
        print(".ASPXAUTH:", aspxauth, end='\n\n')

        return asp_net_session_id, aspxauth
    else:
        print("Erro ao obter cookies. Código de status:", response.status_code)
        return None, None





login = login_conf
senha = senha_conf

#login_safra(login, senha, session,)
#cookies_safra(login, senha, verification_token, session, __RequestVerificationToken, NSC_WJQ_GJOBODFJSB_FQGXFC_443, _abck, ak_bmsc, bm_sv, bm_sz, ASP_NET_SessionId, notifier, bm_mi)

_abck, ak_bmsc, bm_mi, bm_sv, bm_sz, NSC_WJQ_GJOBODFJSB_FQGXFC_443, __RequestVerificationToken, verification_token, notifier, session, ASP_NET_SessionId = login_safra(login, senha, session)
cookies_safra(login, senha, verification_token, session, __RequestVerificationToken, NSC_WJQ_GJOBODFJSB_FQGXFC_443, _abck, ak_bmsc, bm_sv, bm_sz, ASP_NET_SessionId, notifier, bm_mi)