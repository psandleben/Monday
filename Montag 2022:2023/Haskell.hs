import Distribution.Simple.Utils (xargs)
mal2 :: Int -> Int
mal2 n = n * 2

quadrat :: Int -> Int
quadrat n = n * n

zweiHoch :: Int -> Int
zweiHoch 1 = 1
zweiHoch n = 2 * zweiHoch (n-1)

fakultät :: Int -> Int
fakultät 0 = 1
fakultät n = n * fakultät (n-1)

mHochN :: Int -> Int -> Int
mHochN x 0 = 1
mHochN x n = x * mHochN x (n-1)

fibonacci :: Int -> Int
fibonacci 1 = 1
fibonacci 2 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)


-- mode x y = x % y
-- div x y = x // y

--quersumme :: Int -> Int
--quersumme 0 = 0
--quersumme x = mod x 10 + quersumme div x 10

erstes :: [Int] -> Int
erstes [] = error "Alles am Arsch"
erstest (x:xs) = x

letztes :: [Int] -> Int
letztes [] = error "Alles am Arsch"
letztes [x] = x
letztes (x : xs) = letztes xs

summe :: [Int] -> Int
summe [] = 0
summe (x:xs) = x + summe xs

länge :: [Int] -> Int
länge [x] = 0
länge (x:xs) = 1 + länge xs

nimm :: [Int] -> Int -> Int
nimm (x : xs) 1 = x
nimm (x: xs) n = nimm xs (n-1)

umdrehen :: [Int] -> [Int]
umdrehen [x] = [x] 
umdrehen (x : xs) = umdrehen xs ++ [x]

enthalten :: [Int] -> Int -> Bool
enthalten (x:xs) n
    |x == n = True
    | otherwise = enthalten (xs++[x]) n

entfernen :: [Int] -> Int -> [Int]
entfernen (x:xs) n
    |x == n = xs
    | otherwise = entfernen (xs ++ [x]) n

positiv :: Int -> Bool
positiv n
    | n > 0 = True
    | otherwise = False

kleinstes :: [Int] -> Int
kleinstes [n] = n
kleinstes (x:y:ys)
    | x > y = kleinstes ([y] ++ ys)
    | y >= x = kleinstes ([x] ++ ys)

löschen :: [Int] -> Int -> [Int]
löschen (x:xs) 0 = xs
löschen (x:xs) n = löschen (xs ++ [x]) (n-1) 

anzahl :: [Int] -> Int -> Int
anzahl [] n = 0
anzahl (x:xs) n
    | x == n = 1 + anzahl xs n 
    | otherwise = anzahl xs n

mapper :: (a -> b) -> [a] -> [b]
mapper n [x] = [n x]
mapper n (x:xs) = [n x] ++ mapper n xs

sortiert :: [Int] -> Bool
sortiert [x] = True
sortiert (x:y:ys)
    | x > y = False
    | otherwise = sortiert ([y] ++ ys)

selectionSort :: [Int] -> [Int]
selectionSort n  
    | sortiert n == True = n 
selectionSort (x:y:xs) = 