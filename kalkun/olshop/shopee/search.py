
class Search:

	def hint( keyword:str, params:dict=None, type:int=0, version:int=1 ) -> any:
		
		""" https://shopee.co.id/api/v4/search/search_hint?extra_params={"global_search_session_id":"gs-ace4b4f5-a58a-446c-87ab-89ea40463327"}&keyword=h&search_type=0&version=1 """

	def items() -> any:
		""" https://shopee.co.id/api/v4/search/search_items?by=relevancy&extra_params={"global_search_session_id":"gs-ace4b4f5-a58a-446c-87ab-89ea40463327","search_session_id":"ss-f82ceb59-5170-404a-a4ac-0e0aab741f8b"}&keyword=hijab&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=b9a1e4e9-77ba-4497-82cc-6fae819f345f """

	def suggestion() -> any:
		""" https://shopee.co.id/api/v4/search/search_suggestion?bundle=popsearch&extra_params={"global_search_session_id":"gs-ace4b4f5-a58a-446c-87ab-89ea40463327","search_session_id":"ss-f82ceb59-5170-404a-a4ac-0e0aab741f8b"}&limit=8&offset=0 """

	def user() -> any:
		""" https://shopee.co.id/api/v4/search/search_user?keyword=hijab&limit=1&offset=0&with_search_cover=true """

