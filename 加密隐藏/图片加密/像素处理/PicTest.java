<<<<<<< HEAD
import java.io.BufferedReader;  
import java.io.File;  
import java.io.FileInputStream;  
import java.io.FileNotFoundException;  
import java.io.IOException;  
import java.io.InputStreamReader;  
  
import javax.imageio.ImageIO;  
  
import java.awt.image.BufferedImage;  
  
public class PicTest {  
    public static void main(String[] args) throws IOException {  
        int i,j;  
        int rgb[] = new int[3];  
        File file = new File("1.jpg");
        BufferedImage bi = null; 
        bi = ImageIO.read(file);  
        int width = bi.getWidth();  
        int height = bi.getHeight();  
        int minx = bi.getMinX();  
        int miny = bi.getMinY();  
        for (i = 0; i < width; i++) {  
            for (j = 0; j < height; j++) {  
                int col = 0;  
                int fcol = bi.getRGB(i, j);  
                if ((fcol >>> 9 & 1) > 0)  
                    col = 0xffffff;  
                bi.setRGB(i, j, col);  
            }  
        }  
        ImageIO.write(bi, "JPEG", file); 
    }  
=======
import java.io.BufferedReader;  
import java.io.File;  
import java.io.FileInputStream;  
import java.io.FileNotFoundException;  
import java.io.IOException;  
import java.io.InputStreamReader;  
  
import javax.imageio.ImageIO;  
  
import java.awt.image.BufferedImage;  
  
public class PicTest {  
    public static void main(String[] args) throws IOException {  
        int i,j;  
        int rgb[] = new int[3];  
        File file = new File("1.jpg");
        BufferedImage bi = null; 
        bi = ImageIO.read(file);  
        int width = bi.getWidth();  
        int height = bi.getHeight();  
        int minx = bi.getMinX();  
        int miny = bi.getMinY();  
        for (i = 0; i < width; i++) {  
            for (j = 0; j < height; j++) {  
                int col = 0;  
                int fcol = bi.getRGB(i, j);  
                if ((fcol >>> 9 & 1) > 0)  
                    col = 0xffffff;  
                bi.setRGB(i, j, col);  
            }  
        }  
        ImageIO.write(bi, "JPEG", file); 
    }  
>>>>>>> 0b9dbfb320a073901bf33fe49fb8fcc85520109c
}  