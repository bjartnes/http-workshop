var client = new HttpClient();
var response = await client.GetStringAsync("http://localhost:6666/foobar");
Console.WriteLine(response);
