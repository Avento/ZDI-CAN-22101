# ZDI-CAN-22101
(0Day) Microsoft Exchange CreateAttachmentFromUri Server-Side Request Forgery Information Disclosure Vulnerability

## Reference
https://www.zerodayinitiative.com/blog/2023/11/1/unpatched-powerful-ssrf-in-exchange-owa-getting-response-through-attachments

## Stack
```txt
>	System.Net.Http.dll!System.Net.Http.HttpClientHandler.CreateAndPrepareWebRequest(System.Net.Http.HttpRequestMessage request) (IL=prolog, Native=0x00007FFBDC73F120+0x0)
 	System.Net.Http.dll!System.Net.Http.HttpClientHandler.SendAsync(System.Net.Http.HttpRequestMessage request, System.Threading.CancellationToken cancellationToken) (IL≈0x0079, Native=0x00007FFBDC73E990+0x12F)
 	System.Net.Http.dll!System.Net.Http.HttpMessageInvoker.SendAsync(System.Net.Http.HttpRequestMessage request, System.Threading.CancellationToken cancellationToken) (IL≈0x003C, Native=0x00007FFBDC73E800+0x87)
 	System.Net.Http.dll!System.Net.Http.HttpClient.SendAsync(System.Net.Http.HttpRequestMessage request, System.Net.Http.HttpCompletionOption completionOption, System.Threading.CancellationToken cancellationToken) (IL≈0x007F, Native=0x00007FFBDC73DFE0+0x120)
 	System.Net.Http.dll!System.Net.Http.HttpClient.GetAsync(System.Uri requestUri, System.Net.Http.HttpCompletionOption completionOption, System.Threading.CancellationToken cancellationToken) (IL=epilog, Native=0x00007FFBDC73CD10+0x57)
 	Microsoft.Exchange.Clients.Owa2.Server.dll!Microsoft.Exchange.Clients.Owa2.Server.Core.CreateAttachmentFromUri.<>c__DisplayClass9_0.<DownloadAndAttachFileFromUri>b__0(Microsoft.Exchange.Services.RequestDetailsLogger logger) (IL≈0x0088, Native=0x00007FFBDCD19370+0x1B8)
 	mscorlib.dll!System.Runtime.CompilerServices.AsyncTaskMethodBuilder.Start<Microsoft.Exchange.Clients.Owa2.Server.Core.CreateAttachmentFromUri.<>c__DisplayClass9_0.<<DownloadAndAttachFileFromUri>b__0>d>(ref Microsoft.Exchange.Clients.Owa2.Server.Core.CreateAttachmentFromUri.<>c__DisplayClass9_0.<<DownloadAndAttachFileFromUri>b__0>d stateMachine) (IL≈0x002C, Native=0x00007FFBDCD18E70+0x80)
 	Microsoft.Exchange.Clients.Owa2.Server.dll!Microsoft.Exchange.Clients.Owa2.Server.Core.CreateAttachmentFromUri.<>c__DisplayClass9_0.<DownloadAndAttachFileFromUri>b__0(Microsoft.Exchange.Services.RequestDetailsLogger logger) (IL≈0x002B, Native=0x00007FFBDCD18DD0+0x6E)
 	mscorlib.dll!System.Threading.Tasks.Task.Execut e() (IL≈0x0010, Native=0x00007FFBD7AC9110+0x49)
 	mscorlib.dll!System.Threading.ExecutionContext.RunInternal(System.Threading.ExecutionContext executionContext, System.Threading.ContextCallback callback, object state, bool preserveSyncCtx) (IL≈0x0079, Native=0x00007FFBD714FCA0+0x16F)
 	mscorlib.dll!System.Threading.ExecutionContext.Run(System.Threading.ExecutionContext executionContext, System.Threading.ContextCallback callback, object state, bool preserveSyncCtx) (IL=epilog, Native=0x00007FFBD714F3A0+0x14)
 	mscorlib.dll!System.Threading.Tasks.Task.ExecuteWithThreadLocal(ref System.Threading.Tasks.Task currentTaskSlot) (IL=0x00E1, Native=0x00007FFBD7AC8580+0x228)
 	mscorlib.dll!System.Threading.Tasks.Task.ExecuteEntry(bool bPreventDoubleExecution) (IL≈0x0058, Native=0x00007FFBD7AC8460+0xC8)
 	mscorlib.dll!System.Threading.ThreadPoolWorkQueue.Dispatch() (IL=0x00A4, Native=0x00007FFBD7AC7350+0x1C2)


## Screenshot
![first poc ssrf success](https://laughing-markdown-pics.oss-cn-shenzhen.aliyuncs.com/20231106181435.png)
