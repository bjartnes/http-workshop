var app = WebApplication.Create(args);

app.MapGet("/", () => "Hello World!");

app.MapGet("/cancelNotPassingCt", async (CancellationToken ct, ILogger<Program> logger) => 
 	{
		try {
			logger.LogInformation("Incoming request");
			await Task.Delay(10000);
			logger.LogInformation("Finished waiting");
			return "Hello World!";
		} catch (OperationCanceledException ex) {
			logger.LogError("I was cancelled", ex);
			return "I was cancelled...";
		}
 	});

app.MapGet("/cancelPassingCt", async (CancellationToken ct, ILogger<Program> logger) => 
 	{
		try {
			logger.LogInformation("Incoming request");
			await Task.Delay(10000, ct);
			logger.LogInformation("Finished waiting");
			return "Hello World!";
		} catch (OperationCanceledException ex) {
			logger.LogError("I was cancelled", ex);
			return "I was cancelled...";
		}
 	});


app.Run("http://localhost:3000");
