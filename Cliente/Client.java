import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.io.IOException;

public class Client
{
    public static void main(String[] args)
    {
        try(com.zeroc.Ice.Communicator communicator = com.zeroc.Ice.Util.initialize(args))
        {
            com.zeroc.Ice.ObjectPrx base = communicator.stringToProxy("Cara:default -p 10000");
            Demo.CaraPrx cara = Demo.CaraPrx.checkedCast(base);
            if(cara == null)
            {
                throw new Error("Invalid proxy");
            }

	    try{
                Path path = Paths.get(args[0]);
                byte[] bArray = Files.readAllBytes(path);
                System.out.println(cara.getCaras(bArray));
            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }
}

