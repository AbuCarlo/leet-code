
scalaVersion := "2.11.11"

resolvers += "Sonatype OSS Snapshots" at
  "https://oss.sonatype.org/content/repositories/releases"

scalacOptions in ThisBuild ++= Seq("-Xexperimental", "-deprecation")

libraryDependencies ++= Seq(
  "org.log4s" %% "log4s" % "1.3.5",
  "org.scala-graph" %% "graph-core" % "1.12.1",
  "ch.qos.logback" % "logback-classic" % "1.1.11",
  "org.scalatest" %% "scalatest" % "2.2.4" % Test,
  "org.scalacheck" %% "scalacheck" % "1.12.1" % Test,
  "junit" % "junit" % "4.10" % Test
)

fork in run := true
