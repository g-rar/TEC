package app;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URISyntaxException;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class CommandInterface {

	private static Facade program = new Facade();
	private static CommandDataSaver cmds = new CommandDataSaver();

	public static void main(String[] args) {
		try {
			
			Map<String, Runnable> commands = new HashMap<>();
			commands.put("indexar", () -> indexar(args));
			commands.put("cargar", () -> cargar(args));
			commands.put("buscar", () -> buscar(args));
			commands.put("establecer", () -> establecer(args));
			
			if(!args[0].equals("install")) {
						
				if(commands.containsKey(args[0])) {
					loadData();
					if (!args[1].equals("-h"))
						commands.get(args[0]).run();
					else
						printHelp();	
				} else {
					System.out.println(args[0] + " no se reconoce como un comando del programa.");
				}	
			} else {
				instalar(commands.keySet());
			}
			
			
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Por favor, ingrese parámetros. Puede ingresar -h para leer ayuda.");
		}
	}

	private static void loadData() {
		try {
			if(!cmds.getCalc().isEmpty()) 
				program.setCalculator(cmds.getCalc());
			if(!cmds.getSaveDataDir().isEmpty())
				program.setDataSaveDir(cmds.getSaveDataDir());
			if(!cmds.getIndexerPath().isEmpty())
				program.setIndexer(cmds.getIndexerPath());
		} catch (IOException e) {
			System.out.println("Algo salió mal a la hora de cargar los datos. EStos son los datos del error:");
			e.printStackTrace();
		}
	}

	private static void indexar(String[] args) {
		try {
			if (!args[1].equals("-f")) {
				System.out.println(args[1] + " no se reconce como un subcomando para 'indexar'.\n"
						+ "Puede ingresar -h para leer ayuda.");
				return;
				}
			String pPath = "";
			for (int i = 2; i < args.length; i++) {
				pPath = pPath + args[i] + " ";
			}
			pPath = pPath.substring(0, pPath.length() - 1);

			program.index(pPath);
			program.saveIndex();

		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("\nHacen falta parámetros. Puede ingresar -h para leer ayuda.");
		} catch (SQLException e) {
			System.out.println(
					"\nHa ocurrido un error. Puede que el directorio que haya ingresado no sea válido. Intente de nuevo.");
		} catch (InterruptedException e) {
			System.out.println("\nLa operación ha sido interrumpida, por favor intente de nuevo.");
		} catch (IOException e) {
			System.out.println(
					"\nHa ocurrido un error. Puede que el directorio que haya ingresado no sea válido. Intente de nuevo.");
		} catch (Exception e) {
			System.out.println("\nNo se ha establecido una carpeta en la que guardar la información de los archivos indexados.");
			e.printStackTrace();
		}
	}

	private static void cargar(String[] args) {
		try {
			if (!args[1].equals("-p")) {
				System.out.println("\n" + args[1] + " no se reconce como un subcomando para 'cargar'.\n"
						+ "Puede ingresar -h para leer ayuda.");
				return;
			}
			String pPath = "";
			for (int i = 2; i < args.length; i++) {
				pPath = pPath + args[i] + " ";
			}
			pPath = pPath.substring(0, pPath.length() - 1);
			program.setIndexer(pPath);
			cmds.setIndexerPath(pPath);
			cmds.updateData();
			
			System.out.print("Se cargó el indexador en " + pPath);

		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("\nHacen falta parámetros. Puede ingresar -h para leer ayuda.");
		} catch (IOException e) {
			System.out.println(
					"\nHa ocurrido un error. Puede que el directorio que haya ingresado no sea válido. Intente de nuevo.");
		}
	}

	private static void buscar(String[] args) {
		try {
			if (!args[1].equals("-q")) {
				System.out.println("\n" + args[1] + " no se reconce como un subcomando para 'buscar'.\n"
						+ "Puede ingresar -h para leer ayuda.\n");
				return;
			}
			if (!(args[args.length - 2].equals("-k") & args[args.length - 1].equals("k"))) {
				System.out.println(
						"\nLa sintaxis que ingresó no es válida. Puede ingresar -h para obtener ayuda.");
				return;
			}
			String pQuery = "";
			for (int i = 2; i < args.length - 2; i++) {
				pQuery = pQuery + args[i] + " ";
			}
			pQuery = pQuery.substring(0, pQuery.length() - 1);
			String[] results = program.searchQuery(pQuery);
			System.out.println("\nLos archivos ordenados desde mayor a menor semejanza son los siguientes:\n");
			for (String dir : results) {
				System.out.println(dir);
			}
			System.out.print("\n");

		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("\nHacen falta parámetros. Puede ingresar -h para leer ayuda. Estos son los datos del error:\n\n");
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println(
					"\nHa ocurrido un error. Puede que el directorio que haya ingresado no sea válido. Intente de nuevo.");
		} catch (NullPointerException e) {
			System.out.println(
					"\nFaltan datos para hacer la búsqueda. Es necesario cargar la información de los archivos indexados y establecer una calculadora.");
		}
	}

	private static void establecer(String[] args) {
		try {
			if (args[1].equals("-c")) {
				program.setCalculator(args[2]);
				cmds.setCalc(args[2]);
				cmds.updateData();
				System.out.println("Se ha establecido " + args[2] + " como método para comparar archivos.");
				
			} else if (args[1].equals("-s")) {
				String pPath = "";
				for (int i = 2; i <= args.length - 1; i++) {
					pPath = pPath + args[i] + " ";
				}
				pPath = pPath.substring(0, pPath.length() - 1);
				program.setDataSaveDir(pPath);
				cmds.setSaveDataDir(pPath);
				cmds.updateData();
				System.out.println("Se ha establecido " + pPath + " como directorio para guardar datos de archivos indexados.");

			} else {
				System.out.println(
						args[1] + " no se reconce como un subcomando para 'cargar'. Puede ingresar -h para leer ayuda.");
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Hacen falta parámetros. Puede ingresar -h para leer ayuda.");
		} catch (IOException e) {
			System.out.println("La ruta o calculadora indicadas no son válidas.");
		}
	}
	
	private static void instalar(Set<String> commands) {
		String installPath;
		try {
			installPath = new File(CommandInterface.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getPath();
			for( int i = installPath.length() - 1 ; i > 0 ; i--) {
				if(installPath.charAt(i) == '\\') {
					installPath = installPath.substring(0, i);
					break;
				}
			}
			
			for(String command : commands) {
				File f = new File(command + ".bat");
				f.createNewFile();
				String batchTemplate = 
						  "@echo off\n"
						+ "set startPath=%CD%\n"
						+ "cd " + installPath + "\n"
						+ "color 70"
						+ "java -jar FilexPlOOrer.jar " + command + " %* \n"
						+ "color 07"
						+ "cd %startpath%";
				FileWriter fw = new FileWriter(f);
				fw.write(batchTemplate);
				fw.close();
			}
		} catch (URISyntaxException e) {
			System.out.println("Un error ha ocurrido. Aquí están los datos del error:\n\n");
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("Un error ha ocurrido. Aquí están los datos del error:\n\n");
			e.printStackTrace();
		}		
		
	}
	
	private static void printHelp() {
		System.out.println("\nAyuda para el indexador/buscador FilexPlOOrer\n" 
				+ "\n establecer -s [directorio] \t\t"
					+ "Establece [directorio] como el lugar donde se guardaran \n"
					+ "\t\t\t\t\t los datos de las carpetas que se indexen.\n" 
				+ "\n establecer -c [cosine/manhattan] \t"
					+ "Establece el método para comparar los archivos indexados.\n" 
				+ "\n indexar -f [directorio] \t\t"
					+ "Recorre una carpeta y sus subcarpetas para indexar los \n" 
					+ "\t\t\t\t\t archivos compatibles.\n"
				+ "\n cargar -p [directorio]\t\t\t" + "Carga el archivo .json indicado en el directorio que \n"
					+ "\t\t\t\t\t contiene la información de los archivos indexados.\n" 
				+ "\n buscar -q [búsqueda] -k k\t\t"
					+ "Muestra en pantalla una lista de archivos donde el \n"
					+ "\t\t\t\t\t primero es el más relacionado a los terminos de [búsqueda]\n");
		System.out.println("\nInformación de las configuraciones actuales:\n"
				+ "\tMétodo de comparación = " + cmds.getCalc() 
				+ "\n\tDirección de guardado = " + cmds.getSaveDataDir() 
				+ "\n\tDatos de la carpeta indexada = " + cmds.getIndexerPath());

	}
}
