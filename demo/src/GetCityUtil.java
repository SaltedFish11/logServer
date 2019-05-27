import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;

public class GetCityUtil {
	public static String getCity(String ip) throws Exception, FileNotFoundException{
        long longIP = getLongIp(ip);
        List<String> list = new ArrayList();
		String city = null;
		String encoding = "utf-8";
        File file = new File("/Users/yangwenrui/Downloads/ip.txt");
        if (file.isFile() && file.exists()){ // 判断文件是否存在
            InputStreamReader read = new InputStreamReader(
                    new FileInputStream(file), encoding);// 考虑到编码格式
            BufferedReader bufferedReader = new BufferedReader(read);
            String lineTxt = null;

            while ((lineTxt = bufferedReader.readLine()) != null)
            {
                String[] split = lineTxt.split("\\|");
                long startIp = getLongIp(split[0]);
                long endIp = getLongIp(split[1]);
                if(longIP>=startIp && longIP<=endIp){
                    city = split[6];
                }
            }
            bufferedReader.close();
            read.close();
        }
        else
        {
            System.out.println("找不到指定的文件");
        }
		return city;
	}
	
	public static void main(String[] args) throws Exception {
        String city = getCity("218.4.129.255");
        System.out.println(city);

    }

    public static long getLongIp(String ip){
        String[] ips = ip.split("\\.");
        long longIP = 0;

	    try {
            if (ips.length == 4) {
                longIP = Integer.parseInt(ips[0])* 256 * 256 * 256
                        + Integer.parseInt(ips[1]) * 256 * 256
                        + Integer.parseInt(ips[2]) * 256
                        + Integer.parseInt(ips[3]);
            }
        }catch (Exception e){
	        e.printStackTrace();
        }
        return longIP;
    }
}
