import requests
import time

f = open("kk.csrf")
exec(f.read())

cook = '''LIVE_BUVID=AUTO2715869494375193; buvid4=23468A39-02F5-F517-C3F3-C888A8C7CE5234256-022110114-h5BQ7Dv0eOwgf7EV4XZm8Q%3D%3D; CURRENT_FNVAL=4048; buvid_fp_plain=undefined; DedeUserID=97258929; DedeUserID__ckMd5=a8301ff9ec818dc4; header_theme_version=CLOSE; enable_web_push=DISABLE; _uuid=73CCD7910-EBFD-3AAD-4E3B-9FCFDE8BCA4D90774infoc; CURRENT_QUALITY=64; is-2022-channel=1; fingerprint=b8880a63e8513ea9be12b24d19902932; buvid3=33E00AA8-F122-6D8D-E856-C4AA4D45F29504000infoc; b_nut=1713419804; buvid_fp=b8880a63e8513ea9be12b24d19902932; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; rpdid=|(kJ|~uJY|JY0J'u~ulY|k)Jl; home_feed_column=5; hit-dyn-v2=1; share_source_origin=COPY; SESSDATA=69eaf460%2C1742636966%2Ce6ad2%2A91CjC_pZw3DTwBVDnNL5fsw-bOdMRe9uTBh7Vq8T-LxDvNMIJbduSQfa7MMWrGrPzZScgSVkNfcjRldGhxMUtyMWNPX1lYRVFDdEFxUEJtT3RsdDZBX0p1cHlJZlZSMW9KTG5ITk9wb1cycHRMUVoxTkVfVi1NZVhMT2JQQVlsZU9kbXFVQjV5elFnIIEC; bili_jct=e8739e91a3b3b150d690a3861ab8a4f6; sid=8hdqe0e3; browser_resolution=1536-703; b_lsid=967A219F_19223D7032C; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0Mzc5NjMsImlhdCI6MTcyNzE3ODcwMywicGx0IjotMX0.lJkIZd4CnvYsBth1mEetCxHGKEfDJpvicWPDyVB4zbw; bili_ticket_expires=1727437903; bsource=search_google; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1727180474; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1727180474; HMACCOUNT=F43945DD3EC2D2D9; bp_t_offset_97258929=980722350016167936; PVID=12'''
def send(text, roomid):
	url = 'https://api.live.bilibili.com/msg/send'
	data = {
		'color': '16777215',
		'fontsize': '25',
		'mode':'1',
                'msg': text,
		'rnd':str(int(time.time())),
		'roomid': roomid,
		'bubble':'0',
		'csrf_token':csrf['csrf_token'],
        'csrf':csrf['csrf']}
	cookie = {'Cookie': cook}

	headers = {'cookie':
'''LIVE_BUVID=AUTO2715869494375193; buvid4=23468A39-02F5-F517-C3F3-C888A8C7CE5234256-022110114-h5BQ7Dv0eOwgf7EV4XZm8Q%3D%3D; CURRENT_FNVAL=4048; buvid_fp_plain=undefined; DedeUserID=97258929; DedeUserID__ckMd5=a8301ff9ec818dc4; header_theme_version=CLOSE; enable_web_push=DISABLE; _uuid=73CCD7910-EBFD-3AAD-4E3B-9FCFDE8BCA4D90774infoc; CURRENT_QUALITY=64; is-2022-channel=1; fingerprint=b8880a63e8513ea9be12b24d19902932; buvid3=33E00AA8-F122-6D8D-E856-C4AA4D45F29504000infoc; b_nut=1713419804; buvid_fp=b8880a63e8513ea9be12b24d19902932; FEED_LIVE_VERSION=V_WATCHLATER_PIP_WINDOW3; rpdid=|(kJ|~uJY|JY0J'u~ulY|k)Jl; home_feed_column=5; hit-dyn-v2=1; share_source_origin=COPY; SESSDATA=69eaf460%2C1742636966%2Ce6ad2%2A91CjC_pZw3DTwBVDnNL5fsw-bOdMRe9uTBh7Vq8T-LxDvNMIJbduSQfa7MMWrGrPzZScgSVkNfcjRldGhxMUtyMWNPX1lYRVFDdEFxUEJtT3RsdDZBX0p1cHlJZlZSMW9KTG5ITk9wb1cycHRMUVoxTkVfVi1NZVhMT2JQQVlsZU9kbXFVQjV5elFnIIEC; bili_jct=e8739e91a3b3b150d690a3861ab8a4f6; sid=8hdqe0e3; browser_resolution=1536-703; b_lsid=967A219F_19223D7032C; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc0Mzc5NjMsImlhdCI6MTcyNzE3ODcwMywicGx0IjotMX0.lJkIZd4CnvYsBth1mEetCxHGKEfDJpvicWPDyVB4zbw; bili_ticket_expires=1727437903; bsource=search_google; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1727180474; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1727180474; HMACCOUNT=F43945DD3EC2D2D9; bp_t_offset_97258929=980722350016167936; PVID=12''',
'origin':'https://live.bilibili.com',
'priority':'u=1, i',
'referer':'https://live.bilibili.com/32172872?hotRank=0&session_id=16c14d8097484487619c2025dd66f2b2_7C1D80DF-2AFD-4AC7-B0F6-7E3D6F8830EF&live_from=77002&visit_id=8oy0lym4axk0',
'sec-ch-ua': '''"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"''',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'''"Windows"''',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'''}
	response = requests.post(url, data=data, cookies = cookie, headers=headers)
rid = 32172872
text = "能吧"

send(text, rid)
